"""
Regressão Linear - Estimar o sálario de um funcionário 
de uma determinada empresa baseado em seus anos de experiência.

Aluno: Cicero Josean
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Importar a base de dados necessária
#Criando a tabela de Dados e visalizando os primeiros elementos
salary_data = pd.read_csv("Salary_Data.csv")
print("\nVisualizando as primeiras linhas da base de dados\n",salary_data.head())

# Separando os dados para a variável independente e para variável dependente 
X = salary_data.iloc[:,:-1].values # x são os anos de experiência
y = salary_data.iloc[:, 1].values  # y são os salários

#mostrando algumas estatísticas da base de dados
print("\nEstatísticas da Base de Dados\n",salary_data.describe())

# Split the data into training/testing sets
X_train = X[:-10]
X_test =  X[-10:]

# Split the targets into training/testing sets
y_train = y[:-10]
y_test = y[-10:]

#Gerando o objeto para a regressão linear 
regr = linear_model.LinearRegression()

# Treinando o modelo usando as configurações de treino padrão
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)

# The coefficients
print('Coeficientes da Regressão Linear: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black') #dados reais
plt.plot(X_test, y_pred, color='blue', linewidth=3) #resultados gerados pelo modelo

plt.xticks(())
plt.yticks(())

plt.show()


saida=np.zeros((y_test.shape[0],2))
print("Comparação de Resultados dos Salários")
print("Previsto x Real")
saida[:,0] = y_pred.round()
saida[:,1] = y_test.round()
#y_pred=np.array([y_pred]).transpose()
#y_test=np.array([y_test]).transpose()
#saida=y_pred+y_test
print(saida)
#print(y_test)























