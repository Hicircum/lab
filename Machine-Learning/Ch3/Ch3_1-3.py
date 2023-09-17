import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_circles, make_moons, make_blobs
import clustering_performance


# Generate data
# X, y = make_circles(n_samples=1000, noise=0.1, factor=0.1)
# X, y = make_moons(n_samples=1000, noise=0.1)
X, y = make_blobs(n_samples=1000, centers=3, n_features=3, random_state=1)

# Cluster data
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_pred = kmeans.predict(X)

# Plot raw data and clustered data
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
colors = ['red', 'green', 'blue']
axs[0].scatter(X[:, 0], X[:, 1], marker="o", edgecolors='black', c=[colors[i] for i in y])
axs[0].set_title('Raw Data')
axs[1].scatter(X[:, 0], X[:, 1], marker="o", edgecolors='black', c=[colors[i] for i in y_pred])
axs[1].set_title('Clustered Data')

# # Calculate clustering metrics
ACC, NMI, ARI = clustering_performance.clusteringMetrics(y, y_pred)
# print(y)
# print(y_pred)

# Output clustering metrics on the plot
axs[1].text(0.05, 0.05, f"ACC: {ACC:.2f}", transform=axs[1].transAxes, fontsize=10, verticalalignment='bottom')
axs[1].text(0.05, 0.10, f"NMI: {NMI:.2f}", transform=axs[1].transAxes, fontsize=10, verticalalignment='bottom')
axs[1].text(0.05, 0.15, f"ARI: {ARI:.2f}", transform=axs[1].transAxes, fontsize=10, verticalalignment='bottom')

# Output the indices of the k nearest neighbors to the clustered data plot
from sklearn.neighbors import NearestNeighbors
k = 1
neigh = NearestNeighbors(n_neighbors=k)
neigh.fit(X)
distances, indices = neigh.kneighbors(kmeans.cluster_centers_)
for i in range(len(indices)):
    axs[1].scatter(X[indices[i], 0], X[indices[i], 1], marker="x", s=100, linewidths=3, color='yellow')

plt.show()