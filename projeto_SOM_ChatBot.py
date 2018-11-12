# -*- coding: utf-8 -*-
"""Exemplo_SOM

Interpretador de Assuntos em Mensagens

"""
'''
import nltk  # Natural Language Toolkit
nltk.download('rslp')  #raiz das palavras
nltk.download('punkt')  #trabalhar com pontuação

# tokenize pega uma string e coloca em um vetor
palavra = nltk.tokenize.word_tokenize('dúvida    carro casa')
print (palavra)
stemmer = nltk.stem.RSLPStemmer()   #pegar o radical da palavra
palavra2 = stemmer.stem('dúvida')
print (palavra2)

import unicodedata
palavra_sem_acento = unicodedata.normalize('NFKD','dúvida').encode('ASCII','ignore').decode('utf-8')
print(palavra_sem_acento)
'''

# Ler lista de emails
msg1 = "Professor, não estou conseguindo eNtender o banco de dados da som"
msg2 = "Professor, eu tenho uma sUgestão para um exercício de regressao linear"
msg3 = "Eu não Entendi o exemplo do K-means da eleição"
msg4 = "Não entendi bem aquele assunto da aula de ontem"
msg5 = "Tenho uma sugestão para melhorar o entendimento do exercício de perceptron"
msg6 = "TENHO DÚVIDA QUANTO AOS EXERCICIOS QUE DEVEMOS ELABORAR PARA A AULA DE AMANHÃ."
msg7 = "AMIGOS, AGUARDO CONTATO NO DISCORDIA CASO POSSAM SUGERIR ALGUNS EXEMPLOS SOBRE K-MEANS ."
msg8 = "ENTENDO QUE OS ALGORÍTIMOS APRESENTADOS EM SALA JÁ NOS CAPACITAM A PERCEBER OS BENEFÍCIOS DA AUTOMACAO DE ROTINAS DE INTERPRETAÇÃO DE DADOS EMPREGANDO MACHINE LEARN."
msg9 = "ESTOU ENVIANDO ALGUNS EXERCICIOS PARA COMPARAR OS ALGORITIMOS SOM, K-MEANS E MLP."
msg10 = "OS INTEGRANTES DA NOSSA TURMA PODERÃO APRENDER COMO APLICAR MODELOS OTIMIZADOS?"
msg11 = "A REGRESSÃO LINEAR E MMQ SAO ELEMENTOS EMBUTIDOS NOS ALGORITIMOS DE MACHINE LEARNING?"
msg12 = "COMO PODEMOS APLICAR O PERCEPTRON?"
msg13 = "QUAIS MODELOS DE OTIMIZAÇAO PODEMOS APLICAR EM SALA?"
msg14 = "OS TESTES DE PARADA PODEM SER APLICADOS PARA MLP E REDES NEURAIS ?"
msg15 = "COMO DEVEMOS DEFINIR O TAMANHO INICIAL DA MATRIZ DE NEURONIO?"
msg16 = "QUAIS CAMADAS ESTÃO PRESENTES NAS REDES NEURAIS"
msg17 = "NAS REDES NEURAIS, COM É FEITO O REPROCESSAMENTO DOS FATORES QUE PONDERAM CADA PESO? "




msgs = [msg1, msg2, msg3, msg4, msg5, msg6, msg7,msg8, msg9, msg10, msg11, msg12, msg13, msg14, msg15, msg16, msg17]
# Definir palavra chave

palavras_chaves = ["duv", "sug", "entend","exerci","model","nota","avalia",
                   "exempl","assunt","Machine","Learning", "aprend","revis", "means",
                   "regres", "som","neura", "perceptron", "MLP", "otimiz"]

X = []
for msg in msgs:
    data = []
    aux = False    #verificar se não encontrou nenhuma palavra chave
    #msg_sem_acento = unicodedata.normalize('NFKD',msg).encode('ASCII','ignore').decode('utf-8')
    #print(msg_sem_acento)
    # Transformação em vetor
    for palavra in palavras_chaves:
        if(palavra.lower() in msg.lower()):
            aux = True
            data.append(1)
        else:
            data.append(0)
    if aux == True:
        # Transformar em matriz
        X.append(data)





# Jogar no SOM

print (X)
# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

# Training the SOM
from minisom import MiniSom
som = MiniSom(x = 10, y = 10, input_len = 20, sigma = 1.0, learning_rate = 0.5)


som.random_weights_init(X)


som.train_random(data = X, num_iteration = 100)


# Visualizing the results
from pylab import bone, pcolor, colorbar, plot, show

entend = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sug = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

pergunta1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
pergunta2 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

w_entend = som.winner(entend)
w_sug = som.winner(sug)

w_pergunta1 = som.winner(pergunta1)
w_pergunta2 = som.winner(pergunta2)
plot(w_entend[0] + 0.5, w_entend[1] +0.5, 'o', markeredgecolor='g', markersize = 10, markeredgewidth = 2)
plot(w_sug[0] + 0.5, w_sug[1] +0.5, 'o', markeredgecolor='r', markersize = 10, markeredgewidth = 2)
plot(w_pergunta1[0] + 0.5, w_pergunta1[1] +0.5, 's', markeredgecolor='g', markersize = 10, markeredgewidth = 2)
plot(w_pergunta2[0] + 0.5, w_pergunta2[1] +0.5, 's', markeredgecolor='r', markersize = 10, markeredgewidth = 2)
show()

import matplotlib.pyplot as plt
plt.axis([0,10,0,10])
plt.text(w_entend[0], w_entend[1], "entend", size=5, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
plt.text(w_sug[0], w_sug[1], "sug", size=5, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
plt.text(w_pergunta1[0], w_pergunta1[1], "perg1", size=7, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )

plt.text(w_pergunta2[0], w_pergunta2[1], "perg2", size=7, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )







