# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:13:50 2019

@author: patrickqueres
"""

import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup

req = requests.get('http://receita.economia.gov.br/orientacao/tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic')
if req.status_code == 200:
    # print('Requisição bem sucedida!')
    content = req.content
    
# Extrai a primeira tabela de alíquotas do site
soup = BeautifulSoup(content, 'html.parser')
table = soup.find("table", {"class":"listing"} )

# Converte a tabela em um dataframe
table_str = str(table)
df = pd.read_html(table_str, header=0, index_col=0)[0]

#Substitui os valores NaN por 0
df = df.replace(np.nan, '0,00')
# df.fillna(0) -- não funcionou...


# Remove o simbolo de % dos valores -- MUITA GAMBIARRA!
meus_headers = list(df)
#for header_atual in meus_headers:
    # print (header_atual)
    # df[header_atual] = df[header_atual].map(lambda x: x.rstrip('%'))
# df['2011'] = df['2011'].map(lambda x: x.rstrip('%'))
df['2011'] = df['2011'].map(lambda x: x.rstrip('%'))
df['2011'] = df['2011'].map(lambda x: x.rstrip('%'))
df['2012'] = df['2012'].map(lambda x: x.rstrip('%'))
df['2013'] = df['2013'].map(lambda x: x.rstrip('%'))
df['2014'] = df['2014'].map(lambda x: x.rstrip('%'))
df['2015'] = df['2015'].map(lambda x: x.rstrip('%'))
df['2016'] = df['2016'].map(lambda x: x.rstrip('%'))
df['2017'] = df['2017'].map(lambda x: x.rstrip('%'))
df['2018'] = df['2018'].map(lambda x: x.rstrip('%'))
df['2019'] = df['2019'].map(lambda x: x.rstrip('%'))


print (df.head(12))

#df.fillna('0')

# Convertendo tabelas para valores numéricos
