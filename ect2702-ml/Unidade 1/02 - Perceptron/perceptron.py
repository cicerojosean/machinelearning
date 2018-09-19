"""
Created on Mon Aug 27 15:31:13 2018

Aluno: Cícero Josean
"""

import numpy as np

entradas  = np.array([[0,0,1],[1,1,0]])  #vetor de entrada de dados
saidas = np.array([-1,1])    #vetor de saida de dados
pesos = np.array([0.4,-0.6,0.6])   #pesos de cada variavel de entrada
erro = np.array([0,0,0])
taxaAprendizagem = 0.4
limiar = 0.5
novas_entradas  = np.array([[1,1,1],[0,0,0],[1,0,0],[0,1,1]])  #valores para gerar a saída
epocas = 100  #define o numero de épocas que serão utilizadas

       

def stepFunction(soma):
    if(soma>=0):            
        print("Saida depois da função de ativação: 1")
        print("Classe 1")
        return 1
    print("Saida depois da função de ativação: -1")
    print("Classe 0")
    return -1

#   calcula a saida com pesos atuais (entrada * pesos)
def calculaSaida(registro):   
    s = registro.dot(pesos)-limiar
    print("Saida antes da função de ativação: ",round(s,2))
    return stepFunction(s)

#encontrar o conjunto de pesos que irão satisfazer o conjunto de dados
def treinar(limiar):
    print("\n________Treinamento__________")
    for e in range(epocas):  
        print("\nÉpoca ",e)
        for i in range (len(saidas)):
            saidaCalculada = calculaSaida(entradas[i])
            erro[i] = (saidas[i] - saidaCalculada)
            #atualizacao dos pesos
            pesos[:] = pesos[:] + (taxaAprendizagem*entradas[i]*erro[i]) 
            print("Peso atualizado: "+ str(pesos[:]))
            #atualização do BIAS(limiar)
            limiar = limiar + (taxaAprendizagem*(-1)*erro[i]) 
            print("Limiar atualizado = ",limiar)
            print("erro = ",erro[:])
        if(all(erro[:]==0)):  #erro igual a zero
            break

print("\nPrograma para implementar um perceptron e mostrar os resultados")     
treinar(limiar)
print("\n_______Rede Neural Treinada________")

print("\nEntradas Dadas:")
print("\nEntrada ",entradas[0])
calculaSaida(entradas[0])
print("\nEntrada ",entradas[1])
calculaSaida(entradas[1])
print("\nEntradas Novas:")
print("\nEntrada ",novas_entradas[0])
calculaSaida(novas_entradas[0])
print("\nEntrada ",novas_entradas[1])
calculaSaida(novas_entradas[1])
print("\nEntrada ",novas_entradas[2])
calculaSaida(novas_entradas[2])
print("\nEntrada ",novas_entradas[3])
calculaSaida(novas_entradas[3])




