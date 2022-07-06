import sqlite3

# ---------------------------------------- CONECTAR -----------------------------------------
def conectar():
    """
    Realizar conexão com o Banco de Dados
    
    Parâmetros:
        Nenhum
    Returns:
        conn: Variável de conexão com o Banco de Dados
        cursor: Variável para navegar pelo banco de dados executando os comandos em SQL
    """
    conn = sqlite3.connect("Pet_Lov.db")
    cursor = conn.cursor()
    return conn,cursor

# ---------------------------------------- REGISTRAR ----------------------------------------
def Registrar_Usuario(nome,email,senha,tipo):
    """
    Realizar registro do Usuário no Banco de dados
    
    Parâmetros:
        nome: Nome do Usuário
        email: E-mail do Usuário 
        senha: Senha do Usuário
        tipo: Tipo de Usuário (privilégio Administrador ou Funcionário)
    Returns:
        nenhum
    """
    conn,cursor = conectar() 
    cursor.execute("""
        INSERT INTO Usuarios (NOME_usuario,EMAIL_usuario,SENHA_usuario,TIPO_usuario)
        VALUES (?,?,?,?)
    """, (nome,email,senha,tipo)) 

    conn.commit() 
    conn.close() 

def Registrar_Pessoa(nome,rua,num,bairro,cidade,tel,email,cpf,tipo):
    """
    Realizar registro de Pessoa no Banco de dados
    
    Parâmetros:
        nome: Nome do Usuário
        rua: Nome da Rua de moradia
        num: Número da Casa
        bairro: Bairro de moradia 
        cidade: Cidade de moradia
        tel: Telefone do Usuário
        email: E-mail do Usuário 
        cpf: CPF do Usuário
        tipo: Tipo de Usuário (Adotante, Voluntário ou Ambos)
    Returns:
        nenhum
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
    Realizar registro do Pet no Banco de dados
    
    Parâmetros:
        nome: Nome do Pet
        raca: Raça do Pet 
        genero: Gênero do Pet
        idade: Idade do Pet 
        status: Status do Pet (Liberado, Não Liberado)
        foto: Diretório da foto do Pet. Por padrão é colocado como string vazia
    Returns:
        nenhum
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
    Realizar registro do Lar Temporário no Banco de dados
    
    Parâmetros:
        status: Status do Lar Temporário
        capacidade: Capacidade do Lar Temporário 
        utilizacao: Utilizacao do Lar Temporário
        endereco: Endereço do Lar Temporário
        cod_pessoa: ID(Código) do Usuráio responsável pelo Lar Temporário
    Returns:
        nenhum
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
    Realizar registro de Clínica de Parceiros no Banco de dados
    
    Parâmetros:
        nome: Nome da Clínica
        cnpj: CNPJ da Clínica 
        tel: Telefone da Clínica
        endereco: Endereço da Clínica
    Returns:
        nenhum
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Clinica_vet (NOME_clini,CNPJ_cli,TELEFONE_cli,END_cli)
        VALUES (?,?,?,?)
    """, (nome,cnpj,tel,endereco))
    
    conn.commit()
    conn.close()
    
def Registrar_Adocao(data,status,cod_pet,cod_pessoa):
    """
    Realizar registro de Adoção no Banco de dados
    
    Parâmetros:
        data: Data de visita
        status: Status da Adoção (Aprovada,Reprovada) 
        cod_pet: ID(Código) do Pet a ser Adotado
        cod_pessoa: ID(Código) do Usuário que irá Adotar
    Returns:
        nenhum
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO ADOTA_ADOCAO (DATA_adocao,STATUS_adocao,FK_Pet_COD_pet,FK_Cad_pessoa_COD_pessoa)
        VALUES (?,?,?,?)
    """, (data,status,cod_pet,cod_pessoa))
    
    conn.commit()
    conn.close()

def Registrar_Atendimento(historico,valor,cod_clini,cod_pet):
    """
    Realizar registro de Atendiemento em Clínica Parceira no Banco de dados
    
    Parâmetros:
        historico: Serviços realizados
        valor: Valor do serviço realizado
        cod_clini: ID(Código) da Clínica onde foi feito o serviço
        cod_pet: ID(Código) do Pet em questão
    Returns:
        nenhum
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Procedimento_ATENDER (HISTORICO_proced, VALOR_proced, fk_Clinica_vet__COD_clini, fk_Pet_COD_pet)
        VALUES (?,?,?,?)
    """, (historico,valor,cod_clini,cod_pet))
    
    conn.commit()
    conn.close()

# ---------------------------------------- VERIFICAR ----------------------------------------
def Verificar_Login(email,senha):
    """
    Faz consulta no Banco de Dados com as informações de Login, 
    para ver se o usuário está cadastrado ou não e se sua senha está correta
    
    Parâmetros:
        email: E-mail de Login
        senha: Senha de Login
    Returns:
        VerificaLogin: variável que irá conter o registro encontrado ou vazio se não encontrar nenhum registro
    """
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Usuarios 
            WHERE (EMAIL_usuario = ? AND SENHA_usuario = ?)
        """,(email, senha))
    VerificaLogin = cursor.fetchone()
    conn.close()
    
    return VerificaLogin
    
def Verificar_Admin(email,senha):
    """
    Faz consulta no Banco de Dados com as informações de Login, 
    para ver se o usuário está cadastrado ou não e se sua senha está correta 
    e se esse usuário possui privilégio de administrador 
    
    Parâmetros:
        email: E-mail de Login
        senha: Senha de Login
    Returns:
        VerificaLogin: variável que irá conter o registro encontrado ou vazio se não encontrar nenhum registro
    """
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Usuarios 
            WHERE (EMAIL_usuario = ? AND SENHA_usuario = ? AND TIPO_usuario = 'Administrador')
        """,(email,senha))
    VerificaAdmin = cursor.fetchone()
    conn.close()
    
    return VerificaAdmin

# ---------------------------------------- BUSCAS -------------------------------------------
def buscar_pet(id):
    """
    Busca Pet específico cadastrado no banco de dados
    
    Parâmetros:
        id: ID(Código) do Pet
    Returns:
        result: Registro do Pet  
    """
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Pet WHERE COD_pet = ? 
        """,(str(id)))
    result = cursor.fetchone()
    conn.close()
    
    return result

def buscar_historico_pet(id):
    """
    Busca Historico de Consultas de Pet específico cadastrado no banco de dados
    
    Parâmetros:
        id: ID(Código) do Pet
    Returns:
        result: Registro do historico de consultas do Pet
    
    """
    
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
    """
    Busca lista de clinicas cadastradas no banco de dados
    
    Parâmetros:
        nenhum
    Returns:
        result: Lista com todas as clínicas cadastradas, sem repetição
    
    """
    
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT DISTINCT NOME_clini, COD_clini FROM Clinica_vet
        """)
    result = cursor.fetchall()
    conn.close()
    
    return result

def busca_situacoes_adocao():
    """
    Busca lista de status de Adoções cadastradas no banco de dados
    
    Parâmetros:
        nenhum
    Returns:
        result: Lista com os Status de Adoçao existentes, sem repetição
    
    """
    
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT DISTINCT STATUS_adocao FROM ADOTA_ADOCAO
        """)
    result = cursor.fetchall()
    conn.close()
    
    return result

def busca_situacoes_lares():
    """
    Busca lista de status de Lares Temporários cadastradas no banco de dados
    
    Parâmetros:
        nenhum
    Returns:
        result: Lista com os Status de Lar Temporário existentes, sem repetição
    
    """
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT DISTINCT STATUS_lar FROM Lar_temporario
        """)
    result = cursor.fetchall()
    conn.close()
    
    return result

def busca_situacoes_voluntarios():
    """
    Busca lista de Tipos de Pessoas cadastradas no banco de dados
    
    Parâmetros:
        nenhum
    Returns:
        result: Lista com os Tipos de Pessoa existentes, sem repetição
    
    """
    
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT DISTINCT TIPO_CAD_pessoa FROM Cad_pessoa
        """)
    result = cursor.fetchall()
    conn.close()
    
    return result

# ---------------------------------------- LISTAGENS ----------------------------------------
def mostrar_adotantes(filtros={}):
    """
    Busca os registros de Adotantes, passando filtros ou não
    
    Parâmetros:
        (opcional) filtros: Tipo dicionário. Por padrão é colocado como vazio.
    Returns:
        lista: Lista com os registros de Adotantes, filtrados ou não
    
    """
    
    conn,cursor = conectar()
    
    # Construção do Comando em SQL
    comando = "SELECT COD_pessoa,NOME_pessoa,CPF_pessoa,EMAIL_pessoa,END_rua,END_num,END_bairro,END_cidade,TELEFONE_pessoa,TIPO_CAD_pessoa FROM Cad_pessoa"
    
    if filtros != {}:
        comando += " WHERE "
    
        for f in filtros.items():
            if f[0] == "NOME_pessoa":
                comando += "NOME_pessoa LIKE '%{}%' AND ".format(f[1])
            else: 
                comando += str(f[0]) + " = '" + str(f[1]) + "' AND "
        
        comando = comando[:-5]
    
    # Execução do Comando em SQL
    cursor.execute(comando)

    # Construção da Lista para ficar de acordo com a saida desejada
    lista = []
    for linha in cursor.fetchall():
        endereco = linha[4] + ', ' + str(linha[5]) + ', ' + linha[6] + ', ' + linha[7]
        linha = (linha[0],linha[1],linha[2],linha[3], endereco, linha[8], linha[9])
        lista.append(linha)

    conn.close()
    return lista

def mostrar_pets(filtros={},tipos_pets = 'todos'):
    """
    Busca os registros de Pets, passando filtros ou não
    
    Parâmetros:
        (opcional) filtros: Tipo dicionário. Por padrão é colocado como vazio.
        (opcional) tipos_pets: Diz se vão ser mostrados todos pets incluindo Adotados ou 
                               apenas aqueles que estão Liberados ou não Para Adoção. Por padrão
                               é colocado 'todos'
    Returns:
        lista: Lista com os registros de Pets, filtrados ou não
    
    """
    
    conn,cursor = conectar()
    
    # Construção do Comando em SQL
    comando = "SELECT COD_pet,NOME_pet,RACA_pet,GENERO_pet,IDADE_pet,STATUS_pet FROM Pet"
    
    if tipos_pets != 'todos':
        comando += " WHERE STATUS_pet = 'Liberado' OR STATUS_pet = 'Não Liberado'"
    
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
    
    # Execução do Comando em SQL
    cursor.execute(comando)

    #Construção da Lista 
    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)
    
    conn.close()
    return lista

def mostrar_lares(filtros={}):
    """
    Busca os registros de Lares Temporários, passando filtros ou não
    
    Parâmetros:
        (opcional) filtros: Tipo dicionário. Por padrão é colocado como vazio.
    Returns:
        lista: Lista com os registros de Lares Temporários, filtrados ou não, mostrando o nome da Pessoa, não o id
        lista_aux: Lista com os registros de Lares Temporários, filtrados ou não, mostrando tanto o nome da Pessoa quanto o id
    
    """
    
    conn,cursor = conectar()
    
    # Construção do Comando em SQL
    comando = "SELECT COD_larTemporario,fk_Cad_pessoa_COD_pessoa,ENDERECO_lar,STATUS_lar,CAPACIDADE_lar,UTILIZACAO_lar FROM Lar_temporario"
    filtro_nome_pes = False
    
    if filtros != {}:
        comando += " WHERE "
    
        for f in filtros.items():
            if f[0] == "NOME_pessoa":
                filtro_nome_pes = True
            else: 
                comando += str(f[0]) + " = '" + str(f[1]) + "' AND "
        
        comando = comando[:-5]
        
    # Execução do Comando em SQL
    cursor.execute(comando)

    # Construção da Lista
    lista_aux = []
    for linha in cursor.fetchall():
        lista_aux.append(linha)
        
    lista = []
    
    #ADICIONA NOME DAS PESSOAS
    for item in lista_aux:
        
        cursor.execute("""
            SELECT NOME_pessoa FROM Cad_pessoa WHERE COD_pessoa = ?
        """,(str(item[1])))
        nome_pessoa = cursor.fetchone()
             
        lista.append((item[0],nome_pessoa[0],item[2],item[3],item[4],item[5]))
    
    lista_aux_2 = []
    if filtro_nome_pes == True:
        for item in lista:
            if filtros['NOME_pessoa'] in item:
                lista_aux_2.append(item)
    
    if lista_aux_2 != []:
        lista = lista_aux_2

    conn.close()
    
    return lista,lista_aux

def mostrar_adocoes(filtros={}):
    """
    Busca os registros de Adoções, passando filtros ou não
    
    Parâmetros:
        (opcional) filtros: Tipo dicionário. Por padrão é colocado como vazio.
    Returns:
        lista: Lista com os registros de Adoções, filtrados ou não, mostrando o nome da Pessoa e O nome do Pet, não o id da Pessoa e o id do Pet
        lista_aux: Lista com os registros de Adoções, filtrados ou não, mostrando tanto o nome da Pessoa e o nome do Pet quanto o id da Pessoa e o id do Pet    
    """

    conn,cursor = conectar()
    
    # Construção do Comando em SQL
    comando = "SELECT COD_adocao, FK_Cad_pessoa_COD_pessoa, FK_Pet_COD_pet, DATA_adocao, STATUS_adocao FROM ADOTA_ADOCAO"
    filtro_nome_pet = False
    filtro_nome_pessoa = False
    if filtros != {}:
        
        comando += ' WHERE '
            
        for f in filtros.items():
            if f[0] == "NOME_pet":
                filtro_nome_pet = True
            elif f[0] == "NOME_pessoa":
                filtro_nome_pessoa = True
            else: 
                comando += str(f[0]) + " = '" + str(f[1]) + "' AND "
        
        comando = comando[:-5]
    
    # Execução do Comando em SQL
    cursor.execute(comando)

    # Construção da Lista para ficar de acordo com a saida desejada
    lista_aux = []
    for linha in cursor.fetchall():
        lista_aux.append(linha)
    
    #2-COD PET  1-COD PESSOA
    
    #ADICIONA NOME DAS PESSOAS E DOS PETS
    lista = []
    for item in lista_aux:
        
        cursor.execute("""
            SELECT NOME_pessoa FROM Cad_pessoa WHERE COD_pessoa = ?
        """,(str(item[1])))
        nome_pessoa = cursor.fetchone()
        
        cursor.execute("""
            SELECT NOME_pet FROM Pet WHERE COD_pet = ?
        """,(str(item[2])))
        nome_pet = cursor.fetchone()
        
        try:
            lista.append((item[0],nome_pessoa[0],nome_pet[0],item[3],item[4]))
        except:
            lista.append((item[0],nome_pessoa,nome_pet,item[3],item[4]))
    
    #FILTRA PELO NOME DO PET OU DA PESSOA CASO TENHA ESTE FILTRO
    lista_aux_2 = []
    if filtro_nome_pet == True:
        for item in lista:
            if filtros['NOME_pet'] in item:
                lista_aux_2.append(item)
    
    if filtro_nome_pessoa == True:
        for item in lista:
            if filtros['NOME_pessoa'] in item:
                lista_aux_2.append(item)
    
    if lista_aux_2 != []:
        lista = lista_aux_2

    conn.close()
    
    
    return lista,lista_aux

# ---------------------------------------- ALTERAÇÕES ---------------------------------------
def alterar_status_pet(id,status):
    """
    Altera status de um Pet específico
        
    Parâmetros:
        id: ID(Código) do Pet que deseja mudar o status
        status: Novo status que deseja para o Pet
    Returns:
        nenhum
    
    """
    conn,cursor = conectar()
    cursor.execute(""" UPDATE  Pet 
        SET STATUS_pet = ?  
        WHERE COD_pet = ? """,(status,str(id)))
    
    conn.commit()
    conn.close()

def alterar_status_adocao(id,status):
    """
    Altera status de uma Adoção
        
    Parâmetros:
        id: ID(Código) da Adoção que deseja mudar o status
        status: Novo status que deseja para a Adoção
    Returns:
        nenhum
    """
    
    conn,cursor = conectar()
    cursor.execute(""" UPDATE  ADOTA_ADOCAO 
        SET STATUS_adocao = ?  
        WHERE COD_adocao = ? """,(status,str(id)))
    
    conn.commit()
    conn.close()

def alterar_status_lar(id,status):
    """
    Altera status de um Lar Temporário
        
    Parâmetros:
        id: ID(Código) do Lar Temporário que deseja mudar o status
        status: Novo status que deseja para o Lar Temporário
    Returns:
        nenhum
    """
    conn,cursor = conectar()
    cursor.execute(""" UPDATE  Lar_temporario 
        SET STATUS_lar = ?  
        WHERE COD_larTemporario = ? """,(status,str(id)))
    
    conn.commit()
    conn.close()