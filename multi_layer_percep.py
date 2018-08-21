#feito com classe

class Perceptron(object):
    def __init__(self, w):
        self.w = w
    
    def aprender(self, x, taxa_aprend, d):
        'Treina uma rede neural'
        u = float(x[0]) * self.w[0] + float(x[1]) * self.w[1] + float(x[2]) * self.w[2] - 1 * self.w[3] 
        if (u>0):
            y = 1
        else:
            y = -1
        w_novo = []
        for i in range(0,len(self.w),1):
            w_novo.append(self.w[i] + taxa_aprend * x[i]*(d - y))
        self.w = w_novo
        print(self.w)

w0 = 0.4
w1 = -0.6 
w2 = 0.6
taxa_aprend = 0.4
teta = 0.5
w = [w0, w1, w2, teta]

x = [0, 0, 1, -1]
d = -1

p = Perceptron(w)
p.aprender(x, taxa_aprend, d)

x = [1, 1, 0, -1]
d = 1
p.aprender(x, taxa_aprend, d)



#feito como função

# def calcula_u(x, w):
#     'recebe os pesos para calcular o valor de u, o teta esta no vetor w na ultima posicao'
#     return float(x[0]) * w[0] + float(x[1]) * w[1] + float(x[2]) * w[2] - 1 * w[3] 

# def atualiza_w(wi, xi, taxa_aprend, d, y):
#     'Usa o y calculado para encontrar os novos pesos '
#     wi = wi + taxa_aprend * xi*(d - y)
#     return wi

# def treina_padrao(padrao, pesos_e_limiar, classe, taxa_aprend):
#     'Treina uma rede neural'
#     w = pesos
#     u = calcula_u(padrao, w)
#     if (u>0):
#         y = 1
#     else:
#         y = -1
#     for i in range(0,len(w),1):
#         w[i] = atualiza_w(w[i], padrao[i], taxa_aprend, classe, y)
#     return w

# w0 = 0.4
# w1 = -0.6 
# w2 = 0.6
# taxa_aprend = 0.4
# teta = 0.5
# w = [w0, w1, w2, teta]

# x = [0, 0, 1]
# d = -1
# w = treina_padrao(x, w, -1, taxa_aprend, teta) 

# x = [1, 1, 0]
# d = 1
# treina_padrao(x, w, d, taxa_aprend, teta)
# print(w) 





# u = calcula_u(x, w)
# print(u)

# if (u>0):
#     y = 1
# else:
#     y = -1

# d = -1

# w0 = atualiza_w(0, w, taxa_aprend, d, y)
# w1 = atualiza_w(1, w, taxa_aprend, d, y)
# w2 = atualiza_w(2, w, taxa_aprend, d, y)
# w3 = atualiza_w(3, w, taxa_aprend, d, y)



