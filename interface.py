from PySimpleGUI import PySimpleGUI as sg
import functions
from functions import clientes_dados
from functions import cache
#Layout



def tela_de_envio_de_email():
    layout = [
        [sg.Text("ENVIAR E-MAIL PARA:")],
        [sg.Text("ASSUNTO")], [sg.InputText(key="assunto")],
        [sg.Text("MENSAGEM")],[sg.InputText(key="mensagem")],
    ]


        # armazenar valores do contato
    for cliente in clientes_dados.values:
        layout.append([sg.Checkbox(cliente[0],key=cliente[0])])

    for_final=True
    if for_final == True:
        layout.append( [sg.Button("ENVIAR"), sg.Button("Cancelar")],)

    janela = sg.Window("ENVIAR EMAIL", layout,resizable = True)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Cancelar":
            break
        if evento == "ENVIAR":
            for nome in valores:
                if valores[nome] == True:
                    enviar_para=str(nome)
                    mensagem=valores['mensagem']
                    assunto=valores['assunto']
                    functions.identificar_cliente(enviar_para,assunto,mensagem)
                    valores[nome]=False
                else:
                    pass

    janela.close()


def clientes():
    layout = [
        [sg.Text("ENVIAR E-MAIL PARA:")]
    ]


        # armazenar valores do contato
    for cliente in clientes_dados.values:
        layout.append([sg.Checkbox(cliente[0],key=cliente[0])])

    for_final=True
    if for_final == True:
        layout.append( [sg.Button("Salvar"), sg.Button("Cancelar")],)

    janela = sg.Window("Clientes", layout,resizable = True)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Cancelar":
            break
        if evento == "Salvar":
            lista_envio = []
            for nome in valores:
                if valores[nome] == True:
                    enviar_para=str(nome)
                    lista_envio.append(enviar_para)
                else:
                    pass
            functions.cache(lista_envio)

    janela.close()