# K-Means
# from https://www.superdatascience.com/machine-learning/ 

# Part 1 - Data Preprocessing

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Importing the dataset
dataset = pd.read_csv("Mall_Customers.csv")

print("Primeiros dados:")
print(dataset.head(  ))

X = dataset.iloc[:,[3,4]].values
scaler = StandardScaler()
X = scaler.fit_transform(X)   #escalonar os dados
print("Primeiros 6 linhas do banco de dados:")
print(X[0:6,:])


# Fitting K-Means to the dataset
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 5, init = 'random', random_state = 1)
#kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 1)
y_kmeans = kmeans.fit_predict(X)

print("Resultado da Classificação: 10 primeiros registros")
print(y_kmeans[:10]);
print(kmeans.labels_[:10]);

# Visualising the clusters
#plt.scatter(X[:, 0], X[:, 1], s = 100, c = 'red', label = 'Data')

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 50, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 50, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 50, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 50, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 50, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 150, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()