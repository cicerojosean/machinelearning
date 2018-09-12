"""
Regressão Linear - Estimar o sálario de um funcionário 
de uma determinada empresa baseado em seus anos de experiência.

@author: Cicero Josean
"""
import os
from six.moves import urllib

# Importar a base de dados necessária
FILE_TO_DOWNLOAD =  "Salary_Data.csv"
DOWNLOAD_ROOT = "https://github.com/ect-info/ml/raw/master/"
DATA_PATH = "dados/"
DATA_URL = DOWNLOAD_ROOT + DATA_PATH + FILE_TO_DOWNLOAD

def fetch_data(data_url=DATA_URL, data_path=DATA_PATH, file_to_download=FILE_TO_DOWNLOAD):
  if not os.path.isdir(data_path):
    os.makedirs(data_path)
  urllib.request.urlretrieve(data_url, data_path+"Salary_Data.csv")
  
fetch_data()

import pandas as pd

def load_data(data_path=DATA_PATH, file_to_download=FILE_TO_DOWNLOAD):
  csv_path = os.path.join(data_path,file_to_download)
  return pd.read_csv(csv_path)

#Criando a tabela de Dados e visalizando os primeiros elementos
salary_data = load_data()
print(salary_data.head())

# Separando os dados para a variável independente e para variável dependente 
X = salary_data.iloc[:,:-1].values # x são os anos de experiência
y = salary_data.iloc[:, 1].values  # y são os salários

#mostrando algumas estatísticas da base de dados
print(salary_data.describe())



