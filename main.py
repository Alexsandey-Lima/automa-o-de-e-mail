from PySimpleGUI import PySimpleGUI as sg
from tkinter import Tk
import interface
from interface import tela_de_envio_de_email
root=Tk
layout = [
    [sg.Button("Enviar emails")],
    [sg.Button("Cadastro de clientes")]
]

#monitor_heidht= root.winfo_screenheight
#monitor_widht= root.winfo_screenwidht()
janela = sg.Window("AUTOMAÇÃO DE E-MAIL", layout,resizable = True,size=(1200,40000))

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Enviar emails":
        interface.tela_de_envio_de_email()
    if evento == "Cadastro de clientes":
        interface.clientes()


janela.close()