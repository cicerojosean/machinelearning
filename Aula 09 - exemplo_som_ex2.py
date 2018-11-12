# Importing the libraries
import pandas as pd

# Install MiniSOM
# https://github.com/JustGlowing/minisom 
# Getting Data

# Importing the dataset
dataset = pd.read_csv('perfil_politico.csv')

X = dataset.iloc[:, :].values

print(dataset.head())

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

# Training the SOM
from minisom import MiniSom
som = MiniSom(x = 10, y = 10, input_len = 15, sigma = 1.0, learning_rate = 0.5)
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 150)

esquerda = [[0,1,1,0.5,1,1,0,0,0,0.5,0,0,0.5,0.5,0.5]]
bolsominion = [[1,0,0,0,0,0,1,1,1,1,1,0.5,1,1,0.5]]
glauber = [[0.5,0,0.5,0.5,0,1,0.5,0,0.5,0,0.5,0,0,1,1]]
cicero = [[0,1,1,1,1,1,0,0.5,1,1,0.5,0,0,1,1]]

# Visualizing the results
from pylab import plot, show
w_dir = som.winner(bolsominion)
w_esq = som.winner(esquerda)
w_cic = som.winner(cicero)
w_glau = som.winner(glauber)
plot(w_dir[0] + 0.5, w_dir[1] + 0.5, 'o', markeredgecolor = 'g',
     markersize = 10,   markeredgewidth = 2)
plot(w_esq[0] + 0.5, w_esq[1] + 0.5, 'o', markeredgecolor = 'r',
     markersize = 10,   markeredgewidth = 2)
plot(w_cic[0] + 0.5, w_cic[1] + 0.5, 's', markeredgecolor = 'r',
     markersize = 10,   markeredgewidth = 2)
plot(w_glau[0] + 0.5, w_glau[1] + 0.5, 's', markeredgecolor = 'g',
     markersize = 10,   markeredgewidth = 2)
show()

