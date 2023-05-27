import win32com.client as win32
import pandas as pd
import mensagens
import openpyxl

clientes_dados = pd.read_excel('clientes.xlsx')
cache = pd.read_excel('cache.xlsx')

def enviar_email(cliente,endereco,assunto,mensagem="Hello word"):
    # antes de usar limpar os rascunhos salvos

    # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')

    # criar um email
    email = outlook.CreateItem(0)

    # configurar as informações do seu e-mail
    email.To = endereco
    print(email.To)
    email.Subject = assunto
    email.HTMLBody = mensagem
    email.Send()
    print(f"Email Enviado para {cliente}")

def identificar_cliente(cliente,assunto,mensagem):
    # acessando os contatos

    # escolhe o contato
    # cliente=input("Diga o nomedo usuario para enviar o e-mail\n")

    id = clientes_dados.index[clientes_dados['name'] == cliente].values

    # armazenar valores do contato
    cliente = clientes_dados.iloc[int(id[0]), 0]
    endereco = clientes_dados.iloc[int(id[0]), 1]
    #enviar_email(cliente,endereco,assunto, mensagem)
    print(mensagem)


def cache(lista_chave):
    i=0
    list_cache=[]
    for cliente in lista_chave:
     cache.loc[i,0] = cliente
     list_cache.append(cache.loc[i,0])
     i+=1
    return list_cache

