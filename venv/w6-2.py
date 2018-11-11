from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

from sklearn.cluster import KMeans

iris = datasets.load_iris()
knn = KNeighborsClassifier()
knn.fit(iris.data, iris.target)

t = [5.0, 3.0, 5.0, 2.0]

r = knn.predict([t])
#print(r)

kmeans = KMeans(n_clusters=3).fit(iris.data)

r_kmeans = kmeans.predict(iris.data)

#print(iris.target)
#print(r_kmeans)

"""
=======================
Pie chart on polar axis
=======================

Demo of bar plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt


# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.show()
