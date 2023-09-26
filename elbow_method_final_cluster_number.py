import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

all_silhouette_widths = pd.read_csv('outputs/all_silhouette_widths.csv')

all_sw = pd.DataFrame({'silhouette_widths':all_silhouette_widths['silhouette_widths']})


# Elbow method
k_values = range(1, 11)
inertia_values = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42 ,n_init=10)
    kmeans.fit_predict(all_sw)
    inertia_values.append(kmeans.inertia_)


plt.plot(k_values, inertia_values, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Curve: Inertia vs. Number of Clusters')
plt.grid(True)

plt.savefig("figures/final optimal cluster based on elbow method.png", dpi=300, bbox_inches='tight')


plt.show()

# Find the optimal number of clusters based on the elbow method
optimal_k_elbow = k_values[np.argmin(inertia_values)]
print(f"Optimal number of clusters based on elbow method: {optimal_k_elbow}")
