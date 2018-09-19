"""
Aluno: Cicero Josean

O objetivo da SVM é a partir de uma base de dados de filmes que são produzidos,
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

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0, C = 0.1)
print(classifier)
classifier.fit(X_train, y_train)

# Fazendo a previsão dos Resultados
y_pred = classifier.predict(X_test)

print(y_test[0:2])
print(y_pred[0:2])

# Matriz de Confusão
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão Inicial: \n",cm)
print("Score = ",(cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])*100,"%")


param_grid = {'C':[1,10,100,1000],'gamma': [1,0.1,0.01,0.001],'kernel':['rbf']}
#altera os parâmetros acima, nessa faixa de valores definidos
#parâmetro C = controla o custo de classificações erradas. Quanto maior, mais o modelo penaliza as classificações erradas. Fica mais preciso 
#parâmetro gama = tipo do kernel que está utilizando. Altera o comportamento da função. Baixo gama, gaussiana com alta variancia.  
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)
#refit = permitir que o modelo se fit novamente
#verbose = altera os outputs do programa ao longo da forma como ele está se otimizando
grid.fit(X_train,y_train)
print("Melhores Parâmetros: \n",grid.best_params_) #visualiza os melhores parâmetros encontrados
pred = grid.predict(X_test)  #compara o desempenho com o Y _test
print('\n')
print("Matriz de Confusão:\n",confusion_matrix(y_test, pred))
print("Melhor Score: ", round((grid.best_score_)*100,2),"%")











