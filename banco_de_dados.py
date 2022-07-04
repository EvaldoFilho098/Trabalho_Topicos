import sqlite3
from tkinter import messagebox

from numpy import result_type
"""
    CREATE TABLE "Usuarios" (
	"ID_usuario"	INTEGER NOT NULL UNIQUE,
	"NOME_usuario"	TEXT NOT NULL,
	"EMAIL_usuario"	TEXT NOT NULL,
	"SENHA_usuario"	TEXT NOT NULL,
	"TIPO_usuario"	TEXT NOT NULL,
	PRIMARY KEY("ID_usuario" AUTOINCREMENT)
    );
"""

def conectar():
    conn = sqlite3.connect("Pet_Lov.db")
    cursor = conn.cursor()
    return conn,cursor

# inserindo dados na tabela
def Registrar_Usuario(nome,email,senha,tipo):
    """
    NOME_usuario,EMAIL_usuario,SENHA_usuario,TIPO_usuario
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Usuarios (NOME_usuario,EMAIL_usuario,SENHA_usuario,TIPO_usuario)
        VALUES (?,?,?,?)
    """, (nome,email,senha,tipo))
    #
    conn.commit()
    conn.close()

    #return id

def Registrar_Pessoa(nome,rua,num,bairro,cidade,tel,email,cpf,tipo):
    """
    NOME_pessoa,END_rua,END_num,END_bairro,END_cidade,TELEFONE_pessoa,EMAIL_pessoa,CPF_pessoa,TIPO_CAD_pessoa
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Cad_Pessoa (NOME_pessoa,END_rua,END_num,END_bairro,END_cidade,TELEFONE_pessoa,EMAIL_pessoa,CPF_pessoa,TIPO_CAD_pessoa)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (nome,rua,num,bairro,cidade,tel,email,cpf,tipo))
    
    conn.commit()
    conn.close()

def Registrar_Pet(nome,raca,genero,idade,status,foto=''):
    """
    NOME_pet,RACA_pet,GENERO_pet,IDADE_pet,STATUS_pet,FOTO_pet
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Pet (NOME_pet,RACA_pet,GENERO_pet,IDADE_pet,STATUS_pet,FOTO_pet)
        VALUES (?,?,?,?,?,?)
    """, (nome,raca,genero,idade,status,foto))
    
    conn.commit()
    conn.close()

def Registrar_Lar_Temp(status,capacidade,utilizacao,endereco,cod_pessoa):
    """
    STATUS_lar,CAPACIDADE_lar,UTILIZACAO_lar,ENDERECO_lar,fk_Cad_pessoa_COD_pessoa
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Lar_temporario (STATUS_lar,CAPACIDADE_lar,UTILIZACAO_lar,ENDERECO_lar,fk_Cad_pessoa_COD_pessoa)
        VALUES (?,?,?,?,?)
    """, (status,capacidade,utilizacao,endereco,cod_pessoa))
    
    conn.commit()
    conn.close()

def Registrar_Clinica(nome,cnpj,tel,endereco):
    """
    NOME_clini,CNPJ_clini,TELEFONE_clini,END_clini
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Clinica_vet (NOME_clini,CNPJ_clini,TELEFONE_clini,END_clini)
        VALUES (?,?,?,?)
    """, (nome,cnpj,tel,endereco))
    
    conn.commit()
    conn.close()
    
def Registrar_Adocao(data,status,cod_pet,cod_pessoa):
    """
    DATA_adocao,STATUS_adocao,FK_Pet_COD_pet,FK_Cad_pessoa_COD_pessoa
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO ADOTA_ADOCAO (DATA_adocao,STATUS_adocao,FK_Pet_COD_pet,FK_Cad_pessoa_COD_pessoa)
        VALUES (?,?,?,?)
    """, (data,status,cod_pet,cod_pessoa))
    
    conn.commit()
    conn.close()

def Registrar_Hospedagem(periodo,cod_pet,cod_lar):
    """
    PERIODO_hosp,fk_Pet_COD_pet,fk_Lar_temporario_COD_larTemporario
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Hospedagem_CONTEM (PERIODO_hosp,fk_Pet_COD_pet,fk_Lar_temporario_COD_larTemporario)
        VALUES (?,?,?,?,?,?,?)
    """, (periodo,cod_pet,cod_lar))
    
    conn.commit()
    conn.close()

def Registrar_Atendimento(historico,valor,cod_clini,cod_pet):
    """
    HISTORICO_proced, VALOR_proced, fk_Clinica_vet__COD_clini, fk_pet_COD_pet
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Procedimento_ATENDER (HISTORICO_proced, VALOR_proced, fk_Clinica_vet__COD_clini, fk_Pet_COD_pet)
        VALUES (?,?,?,?)
    """, (historico,valor,cod_clini,cod_pet))
    
    conn.commit()
    conn.close()

def Verificar_Login(email,senha):
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Usuarios 
            WHERE (EMAIL_usuario = ? AND SENHA_usuario = ?)
        """,(email, senha))
    VerificaLogin = cursor.fetchone()
    conn.close()
    
    return VerificaLogin
    
    '''
    try: 
        if login in VerificaLogin and senha in VerificaLogin:
            messagebox.showinfo(title="Login Info", message="Seja Bem Vindo!")
    except:
        messagebox.showerror(title="Login Info",message="Este usuário não está cadastrado!")
    '''

def Verificar_Admin(email,senha):
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Usuarios 
            WHERE (EMAIL_usuario = ? AND SENHA_usuario = ? AND TIPO_usuario = 'Administrador')
        """,(email,senha))
    VerificaAdmin = cursor.fetchone()
    conn.close()
    
    return VerificaAdmin

def buscar_pet(id):
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Pet WHERE COD_pet = ? 
        """,(str(id)))
    result = cursor.fetchone()
    conn.close()
    
    return result

def buscar_historico_pet(id):
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Procedimento_ATENDER WHERE fk_Pet_COD_pet = ? 
        """,(str(id)))
    result_pet = cursor.fetchall()

    for item in range(len(result_pet)):
        cursor.execute(""" 
                SELECT NOME_clini FROM Clinica_vet WHERE COD_clini = ? 
            """,(str(result_pet[item][3])))
        result = cursor.fetchall()
        result_pet[item] = (result_pet[item][0],result[0][0],result_pet[item][1],result_pet[item][2])

    conn.close()
    
    return result_pet

def busca_clinicas():
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT DISTINCT NOME_clini, COD_clini FROM Clinica_vet
        """)
    result = cursor.fetchall()
    conn.close()
    
    return result

def mostrar_adotantes(filtros={}):
    conn,cursor = conectar()
    comando = "SELECT COD_pessoa,NOME_pessoa,CPF_pessoa,EMAIL_pessoa,END_rua,END_num,END_bairro,END_cidade,TELEFONE_pessoa,TIPO_CAD_pessoa FROM Cad_pessoa"
    
    #print(comando)
    if filtros != {}:
        comando += " WHERE "
    
        for f in filtros.items():
            if f[0] == "NOME_pessoa":
                comando += "NOME_pessoa LIKE '%{}%' AND ".format(f[1])
            else: 
                comando += str(f[0]) + " = '" + str(f[1]) + "' AND "
        
        comando = comando[:-5]
        
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        endereco = linha[4] + ', ' + str(linha[5]) + ', ' + linha[6] + ', ' + linha[7]
        linha = (linha[0],linha[1],linha[2],linha[3], endereco, linha[8], linha[9])
        lista.append(linha)

    conn.close()
    return lista

def mostrar_pets(filtros={},tipos_pets = 'todos'):
    conn,cursor = conectar()
    comando = "SELECT COD_pet,NOME_pet,RACA_pet,GENERO_pet,IDADE_pet,STATUS_pet FROM Pet"
    
    if tipos_pets != 'todos':
        comando += " WHERE STATUS_pet = 'Liberado' OR STATUS_pet = 'Não Liberado'"
    #print(comando)
    
    if filtros != {}:
        if 'WHERE' not in comando:
            comando += ' WHERE '
        else:
            comando += ' AND '
            
        for f in filtros.items():
            if f[0] == "NOME_pet":
                comando += "NOME_pet LIKE '%{}%' AND ".format(f[1])
            elif f[0] == "RACA_pet":
                comando += "RACA_pet LIKE '%{}%' AND ".format(f[1])
            else: 
                comando += str(f[0]) + " = '" + str(f[1]) + "' AND "
        
        comando = comando[:-5]
    
    #print(comando)
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)

    #print(lista)
    
    conn.close()
    return lista

def alterar_status_pet(id,status):
    conn,cursor = conectar()
    cursor.execute(""" UPDATE  Pet 
        SET STATUS_pet = ?  
        WHERE COD_pet = ? """,(status,str(id)))
    #result = cursor.fetchone()
    conn.commit()
    conn.close()
    
    #return result