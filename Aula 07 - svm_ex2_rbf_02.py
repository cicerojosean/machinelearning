# -*- coding: utf-8 -*-
"""svm_ex2_rbf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-ykiblraIPEfC2bFo7RMFn7g_ugBj7Wy
"""

# Support Vector Machine (SVM)
# from https://www.superdatascience.com/machine-learning/ 


# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os
from six.moves import urllib

FILE_TO_DOWNLOAD =  "Social_Network_Ads.csv"
DOWNLOAD_ROOT = "https://github.com/ect-info/ml/raw/master/"
DATA_PATH = "dados/"
DATA_URL = DOWNLOAD_ROOT + DATA_PATH + FILE_TO_DOWNLOAD

def fetch_data(data_url=DATA_URL, data_path=DATA_PATH, file_to_download=FILE_TO_DOWNLOAD):
  if not os.path.isdir(data_path):
    os.makedirs(data_path)
  urllib.request.urlretrieve(data_url, data_path+file_to_download)
  
  
fetch_data()

# Importing the dataset
dataset = pd.read_csv(DATA_PATH+FILE_TO_DOWNLOAD)


dataset.head(  )

X = dataset.iloc[:,2:4].values
y = dataset.iloc[:,4].values

print(X[0:6,:])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
print(X_train)
X_train = sc.fit_transform(X_train)  #normalizar os dados
print(X_train)
print(X_test)
X_test = sc.transform(X_test)  #notacao cientifica
print(X_test)


from sklearn.svm import SVC   #Support Vector Classifier 
model = SVC()  #construtor da classe
model.fit(X_train, y_train) 
print(model)
#avaliar o modelo
pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix #comparar os resultados. Métodos usados para avaliar desempenho de um modelo de classificação
print(classification_report(y_test, pred))
print('/n')
print(confusion_matrix(y_test, pred))

#desempenho muito ruim(38%), pq não modificamos os parâmetros
#método para testar uma combinação de parâmetros, encontrar o melhor, e retreinar o modelo
#comom input precisamos de um dicionario, especificando com o que ele vai trabalhar
param_grid = {'C':[0.1,1,10,100,1000],'gamma': [1,0.1,0.01,0.001,0.0001],'kernel':['rbf']}
#altera os parâmetros acima, nessa faixa de valores definidos
#parâmetro C = controla o custo de classificações erradas. Quanto maior, mais o modelo penaliza as classificações erradas. Fica mais preciso 
#parâmetro gama = tipo do kernel que está utilizando. Altera o comportamento da função. Baixo gama, gaussiana com alta variancia.  
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)
#refit = permitir que o modelo se fit novamente
#verbose = altera os outputs do programa ao longo da forma como ele está se otimizando
grid.fit(X_train,y_train)
print(grid.best_params_) #visualiza os melhores parâmetros encontrados
pred = grid.predict(X_test)  #compara o desempenho com o Y _test
print(classification_report(y_test, pred))
print('/n')
print(confusion_matrix(y_test, pred))
# 95% de acerto nos dados de teste
 

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, grid.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('blue', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()