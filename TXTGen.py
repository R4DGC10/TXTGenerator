import tkinter
import os
import time
from tkinter import *
from tkinter import ttk

from tkinter import messagebox



#Icono del Taskbar
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



#Creacion de Ventana y Dimensiones
window = tkinter.Tk()
window.title("Text File Generator")
window.resizable(False, False)
window.iconbitmap(r"Your Icon .ico path")
window.geometry("800x600")

#Contenido
title_main = tkinter.Label(window, text = ".txt file Generator", font = "arial", bg = "green")
title_main.pack(fill = tkinter.X)

label = tkinter.Label(window, text = "Ingrese el nombre del archivo a generar", font = "arial")
label.pack()

name_input = tkinter.Entry(window,  font = "arial")
name_input.pack()

while not name_input:
    msg = tkinter.Label(window,text = "Por favor rellene esta casilla: Nombre de Archivo!")
    name_input = tkinter.Entry(window)
    name_input.pack()

#Pop Up al intentar cerrar
def on_close():
    if messagebox.askokcancel("Saliendo", "¿Está seguro de que desea salir del programa?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_close)


#Funcion define ruta y nombre del archivo.txt
#Compureba que haya un nombre escrito para el archivo

def filename():
    name_doc = name_input.get()
    if not name_doc:
        msg = tkinter.Label(window,text = "Por favor rellene esta casilla: Nombre de Archivo!", font = "arial", bg = "red")
        msg.pack(fill = tkinter.X)
        msg.pack()
        window.after(1500, msg.destroy) 
    else:
        print(name_doc)
        file_name = name_input.get()
        file_path = r"Generate .txt file path"
        create_file(file_path, file_name)

    

Confirm1_button = tkinter.Button(window, text = "Confirmar", command = filename)
Confirm1_button.pack()

#Obtiene Hora
current = time.strftime("%D:%Y:%H:%M:%S", time.localtime())
print(current)

def create_file(file_path, file_name):
    generated_time = current
    file_content = "Archivo Generado via Python/tkinter => " + file_name 
    file_c2 = "Date =>   " + generated_time 
    
    with open(os.path.join(file_path, file_name), 'w' ) as file:
        file.write(file_content +"\n")
        file.write(file_c2+"\n")






#Bucle main de la ventana
window.mainloop()
