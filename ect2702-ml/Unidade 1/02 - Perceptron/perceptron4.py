"""
Created on Mon Aug 27 15:31:13 2018

@author: cicero
"""

import numpy as np

entradas  = np.array([[0,0,1],[1,1,0]])  #vetor de entrada de dados
saidas = np.array([-1,1])    #vetor de saida de dados
pesos = np.array([0.4,-0.6,0.6])   #pesos de cada variavel de entrada
taxaAprendizagem = 0.4
limiar = 0.5
novas_entradas  = np.array([[1,1,1],[0,0,0],[0,1,1]])  #valores para gerar a saída
epocas = 100  #define o numero de épocas que serão utilizadas

def stepFunction(soma):
    if(soma>=1):
        return 1
    return 0

#   calcula a saida com pesos atuais (entrada * pesos)
def calculaSaida(registro):   
    s = registro.dot(pesos)+limiar
    return stepFunction(s)

#encontrar o conjunto de pesos que irão satisfazer o conjunto de dados
def treinar(limiar):
    for e in range(epocas):
        for i in range (len(saidas)):
            saidaCalculada = calculaSaida(entradas[i])
            erro = (saidas[i] - saidaCalculada)
            #atualizacao dos pesos
            pesos[:] = pesos[:] + (taxaAprendizagem*entradas[i]*erro) 
            print("Peso atualizado: "+ str(pesos[:]))
            #atualização do BIAS(limiar)
            limiar = limiar + (taxaAprendizagem*erro) 
        
treinar(limiar)
print("Rede Neural Treinada")

print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(novas_entradas[0]))
print(calculaSaida(novas_entradas[1]))
print(calculaSaida(novas_entradas[2]))




