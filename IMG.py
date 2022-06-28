from tkinter import *
from PIL import Image, ImageTk


# --------------------Função redimensionar img-------------------- #
def redimensionar(img, x, y):
        rimg = img.resize((x, y), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(rimg)
        return new_img