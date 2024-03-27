import requests
from tkinter import *
import ctypes

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_eth = requisicao_dic['ETHBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar:  US$ {cotacao_dolar}
    Euro:  EUR {cotacao_euro}
    Bitcoin:  BTC {cotacao_btc}
    Ethereum:  ETH {cotacao_eth}'''

janela = Tk()
janela.title("Cotação Atual de Moedas")
janela.geometry("320x250")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=30, pady=30)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

janela.iconbitmap("icon.ico")
janela.mainloop()