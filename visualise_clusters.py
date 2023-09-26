import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

covid_scaled = pd.read_csv("outputs/corona_cluster_analysis.csv")

c = covid_scaled['Cluster']

# Determine unique clusters and their associated colors
unique_clusters = np.unique(c)
colors = plt.cm.viridis(np.linspace(0, 1, len(unique_clusters)))  # Adjust the colormap as needed

# Create a custom legend with color patches
legend_patches = [plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color, label=f'Cluster {cluster}')
                  for cluster, color in zip(unique_clusters, colors)]

# Create a figure with two subplots using plt.subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns

# Scatter plot 1
axs[0].grid(True)  # Add grid

axs[0].scatter(covid_scaled['reach'], covid_scaled['closeness'], c=c)
axs[0].set_ylabel('Closeness Centrality')  # Swap y and x labels
axs[0].set_xlabel('Reach Centrality')  # Swap y and x labels


# Scatter plot 2
axs[1].grid(True)  # Add grid

axs[1].scatter(covid_scaled['deep_reach'], covid_scaled['closeness'], c=c)
axs[1].set_ylabel('Closeness Centrality')  # Swap y and x labels
axs[1].set_xlabel('Deep Reach Centrality')  # Swap y and x labels


# Create a single legend for both subplots to the right of the second subplot
fig.legend(handles=legend_patches, title='Cluster', loc='center left', bbox_to_anchor=(1, 0.66))

fig.suptitle('Clusters in Reach and Deep Reach Centrality Compared with Closeness Centrality', fontsize=16, ha='center')


plt.tight_layout()

plt.savefig("figures/Clusters Reach and Deep Reach with Closeness.png", dpi=300, bbox_inches='tight')


plt.show()
