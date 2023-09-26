import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy

cluster_analysis = pd.read_csv("outputs/pca.csv")


distance_matrix = hierarchy.linkage(np.array(cluster_analysis['PCA Component (Corona)']).reshape(-1, 1), method='ward')

# Create a dendrogram
dendrogram = hierarchy.dendrogram(distance_matrix, labels=cluster_analysis['Centrality Measure'].tolist(), orientation='right')

# Customize the plot
plt.title('Dendrogram for Centrality Measures')
plt.xlabel('Distance')

plt.savefig("figures/pca_dendrogram.png", dpi=300, bbox_inches='tight')

# Show the dendrogram
plt.show()

cluster_analysis