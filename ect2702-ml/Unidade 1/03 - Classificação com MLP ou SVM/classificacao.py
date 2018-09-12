"""

@author: cicero
"""
# Support Vector Machine (SVM)
# from https://www.superdatascience.com/machine-learning/ 

# Part 1 - Data Preprocessing

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset =pd.read_csv('dados.csv')
dataset.head()

#X = dataset.iloc[:,[1,2,3,4,6,11,12,21]].values
X = dataset.iloc[:,[6,12]].values
y = dataset.iloc[:,24].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0, C = 0.1)
print(classifier)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

print(y_test[0:35])
print(y_pred[0:35])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão Inicial: /n",cm)
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
print("Melhores Parâmetros: /n",grid.best_params_) #visualiza os melhores parâmetros encontrados
pred = grid.predict(X_test)  #compara o desempenho com o Y _test
print('/n')
print("Matriz de Confusão:",confusion_matrix(y_test, pred))
print("Melhor Score: ",grid.best_score_)











