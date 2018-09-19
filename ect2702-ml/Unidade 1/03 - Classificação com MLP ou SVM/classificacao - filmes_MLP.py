"""
Aluno: Cicero Josean

O objetivo da MLP é a partir de uma base de dados de filmes que são produzidos,
gerar a classificação se um filme tem um bom score ou não (bom é >= 7, e ruim < 7)
"""

import pandas as pd

# Importing the dataset
dataset =pd.read_csv('dados - filmes.csv')
dataset.head()

X = dataset.iloc[:,[1,2,3,4,6,8,9,10]].values
y = dataset.iloc[:,-1].values

newy = []  #vetor que vai classificar o score como bom ou ruim

for i in y:
    if i<7:
        newy.append(0)   #score ruim
    else:
        newy.append(1)   #score bom
        
        
# Separação da base de dados entre Treino e Teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, newy, test_size = 0.25, random_state = 0)

#Normalizando os dados de entrada
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# MultiLayerPerceptronClassifier
from sklearn.neural_network import MLPClassifier 
redeNeural_01 = MLPClassifier(verbose=True) #cria um objeto
redeNeural_01.score #mostra os parâmetros usados no treinamento
redeNeural_01.fit(X_train,y_train) #fazer o treinamento

# Fazendo a previsão dos Resultados
y_pred_01 = redeNeural_01.predict(X_test)

# Matriz de Confusão
from sklearn.metrics import confusion_matrix
cm_01 = confusion_matrix(y_test, y_pred_01)

#Parâmetros Modificados
redeNeural_02 = MLPClassifier(verbose=True,max_iter=1000000,tol=0.000001,activation='logistic')
redeNeural_02.score #mostra os parâmetros usados no treinamento
redeNeural_02.fit(X_train,y_train) #fazer o treinamento

# Fazendo a previsão dos Resultados
y_pred_02 = redeNeural_02.predict(X_test)

# Matriz de Confusão
cm_02 = confusion_matrix(y_test, y_pred_02)

#Comparando os dois Resultados
print("Matriz de Confusão Inicial: \n",cm_01)
score_confusao_01 = (cm_01[0,0]+cm_01[1,1])/(cm_01[0,0]+cm_01[0,1]+cm_01[1,0]+cm_01[1,1])*100
print("Score = ",round(score_confusao_01,2),"%")

print("Matriz de Confusão Modificada: \n",cm_02)
score_confusao_02 = (cm_02[0,0]+cm_02[1,1])/(cm_02[0,0]+cm_02[0,1]+cm_02[1,0]+cm_02[1,1])*100
print("Score = ",round(score_confusao_02,2),"%")




