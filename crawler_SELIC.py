# -*- coding: utf-8 -*-
"""
Instituto de Ciência e Tecnologia (ICT/UFF)
Aluno: Patrick Souza Queres
Data: 06/06/2019

Created on Wed Apr 24 22:13:50 2019
@author: patrickqueres


"""
import requests 
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# Realiza o download da página através da biblioteca request
req = requests.get('http://receita.economia.gov.br/orientacao/tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic')
if req.status_code == 200:
    content = req.content


# Uso do BeautifulSoup para extrair a tabela de class/id "listing" e armazena no objeto table
soup = BeautifulSoup(content, 'html.parser')
table = soup.find("table", {"class":"listing"} )


# Converte a tabela em um dataframe utilizando a biblioteca Pandas
table_str = str(table)
df = pd.read_html(table_str, header=0, index_col=0)[0]


#Substitui os valores "NaN" por 0
df = df.replace(np.nan, '0,00')


# Remove o simbolo de % dos valores
meus_headers = list(df)
for header_atual in meus_headers:
     df[header_atual] = df[header_atual].map(lambda x: x.rstrip('%'))


# imprime os 12 primeiros itens do dataframe
print (df.head(12))

# Converte o dataframe em arquivo CSV
local_do_csv = 'selic.csv'
df.to_csv (local_do_csv, index=True, header=True, encoding="utf-8", sep=";")

print('O arquivo selic.csv foi salvo na pasta do projeto!')