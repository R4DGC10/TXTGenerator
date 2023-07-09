import tkinter
import os
import time
from tkinter import *
from tkinter import ttk

#Creacion de Ventana y Dimensiones
window = tkinter.Tk()
window.title("TXT Creator")
window.iconbitmap(r"C:\Users\cepc2\OneDrive\Desktop\Projects\Python\TXTGen\icono.ico")
window.geometry("800x600")

title_main = tkinter.Label(window, text = ".txt file Generator", bg = "green")
title_main.pack(fill = tkinter.X)

label = tkinter.Label(window, text = "Ingrese el nombre del archivo a generar")
label.pack()

name_input = tkinter.Entry(window)
name_input.pack()

label2 = tkinter.Label(window, text = "Default: Escritorio")
label2.pack()

#Funcion define ruta y nombre del archivo.txt
def filename():
    name_doc = name_input.get()
    print(name_doc)
    file_name = name_input.get()
    file_path = r"C:\Users\cepc2\OneDrive\Desktop"
    create_file(file_path, file_name)
    

Confirm1_button = tkinter.Button(window, text = "Confirmar", command = filename)
Confirm1_button.pack()

#Obtiene Hora
current = time.strftime("%Y:%H:%M:%S", time.localtime())
print(current)

def create_file(file_path, file_name):
    generated_time = current
    file_content = "Archivo Generado via Python/tkinter => " + file_name 
    file_c2 = "Date => " + generated_time 
    
    with open(os.path.join(file_path, file_name), 'w' ) as file:
        file.write(file_content +"\n")
        file.write(file_c2+"\n")






#Bucle main de la ventana
window.mainloop()