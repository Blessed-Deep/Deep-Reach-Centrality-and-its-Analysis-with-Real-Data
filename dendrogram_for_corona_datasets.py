import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy

# Load your data and preprocess as you mentioned
covid_scaled = pd.read_excel("outputs/centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")
covid_scaled = covid_scaled.drop(['Node', 'corona_nodes'], axis=1)

Functions = covid_scaled.columns.tolist()
Functions = [func.replace('_centrality', '') for func in Functions]
index_to_update = Functions.index('approximate_current_flow_betweenness')
Functions[index_to_update] = 'approx_current_flow_betweenness'
covid_scaled.columns = Functions

# Convert the data to a numpy array
data_array = covid_scaled.values

# Calculate the linkage matrix for hierarchical clustering
linkage_matrix = hierarchy.linkage(data_array, method='ward')

# Create dendrogram with function names as labels and rotate it
plt.figure(figsize=(12, 8))
dendrogram = hierarchy.dendrogram(linkage_matrix, labels=covid_scaled.index, orientation='top')  # Rotate to 'left'
plt.title('Dendrogram of COVID-19 Centrality Data')

# Determine the optimal cluster count using the elbow method
# Look for the "elbow point" in the dendrogram
optimal_cluster_count = 10  # Change this to the determined optimal count

# Plot a horizontal line to indicate the optimal cluster count
plt.axhline(y=optimal_cluster_count - 0.5, color='red', linestyle='--', label=f'Optimal Clusters = {optimal_cluster_count}')

plt.legend()
plt.tight_layout()

plt.savefig("figures/all_corona_data_dendrogram.png", dpi=300, bbox_inches='tight')

plt.show()
