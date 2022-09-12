import requests
from tkinter import *

Tk()

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto


janela = Tk()
janela.title('cotação atual das moedas')
janela.geometry("2000x2000")


texto_orientacao = Label(janela, text="clique aqui para ver a cotação das moedas")
texto_orientacao.grid(column = 2000, row = 2000, padx=10, pady=5)

botao=Button(janela, text ='buscar cotações', command= pegar_cotacoes)
botao.grid(column = 0, row = 3, padx= 10, pady= 10)

texto_cotacoes = Label(janela,text="")
texto_cotacoes.grid (column=0, row=2)


janela.mainloop()