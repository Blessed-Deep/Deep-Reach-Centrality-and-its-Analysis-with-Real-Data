import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy


all_silhouette_widths = pd.read_csv('outputs/all_silhouette_widths.csv')


dendro_all_silhouette_widths = pd.DataFrame({'centrality':all_silhouette_widths['centrality'],
                                             'silhouette_widths':all_silhouette_widths['silhouette_widths']})


distance_matrix = hierarchy.linkage(np.array(dendro_all_silhouette_widths['silhouette_widths']).reshape(-1, 1), method='ward')

# Create a dendrogram
dendrogram = hierarchy.dendrogram(distance_matrix, labels=dendro_all_silhouette_widths['centrality'].tolist(), orientation='right')

# Customize the plot
plt.title('Dendrogram for Centrality Measures')
plt.xlabel('Distance')

plt.savefig("figures/silhouette_widths_dendrogram.png", dpi=300, bbox_inches='tight')

# Show the dendrogram
plt.show()

dendro_all_silhouette_widths