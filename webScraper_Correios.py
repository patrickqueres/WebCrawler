# -*- coding: utf-8 -*-
"""

Instituto de Ciência e Tecnologia (ICT/UFF)
Aluno: Patrick Souza Queres
Data: 06/06/2019

Created on Wed May 29 23:21:26 2019
@author: patrickqueres

"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Objeto de dados com o código a ser rastreado
data = {
    'objetos': 'LS873105012CH',
}


# Realiza um POST e download da página através da biblioteca request
url = "https://www2.correios.com.br/sistemas/rastreamento/resultado.cfm"
reposta = requests.post(url, data=data)


# Uso do BeautifulSoup para extrair a tabela de class/id "listing" e armazena no objeto correios
dados = BeautifulSoup(reposta.text, 'html.parser')
correios = dados.find("table", {"class":"listEvent sro"} )


# Converte a tabela em um dataframe utilizando a biblioteca Pandas
table_str = str(correios)
df = pd.read_html(table_str, header=0, index_col=0)[0]

# Imprime os 10 primeiros itens do dataframe
print (df.head(10))

# Criar um arquivo CSV com todo o dataframe gerado
local_do_csv = 'correios.csv'
df.to_csv (local_do_csv, index=True, header=True, encoding="utf-8")