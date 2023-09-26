import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Loading data
covid_scaled = pd.read_excel("outputs/centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")
covid_scaled = covid_scaled.drop(['Node', 'corona_nodes'], axis=1)

# Rename the columns
Functions = covid_scaled.columns.tolist()
Functions = [func.replace('_centrality', '') for func in Functions]
index_to_update = Functions.index('approximate_current_flow_betweenness')
Functions[index_to_update] = 'approx_current_flow_betweenness'
covid_scaled.columns = Functions


centrality_measure_names = covid_scaled.columns.tolist()

# Initialize variables to keep track of silhouette scores and cluster counts
silhouette_scores = []
cluster_counts = list(range(2, 11)) 

# Iterate over different values of k to calculate silhouette scores
for k in cluster_counts:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init = 10)
    kmeans.fit(covid_scaled)
    labels = kmeans.labels_
    silhouette_avg = silhouette_score(covid_scaled, labels)
    silhouette_scores.append(silhouette_avg)

# Find the index of the highest silhouette score
best_cluster_index = silhouette_scores.index(max(silhouette_scores))
best_cluster_count = cluster_counts[best_cluster_index]


# Highlight the function name with the highest silhouette score
best_centrality_measure_name = centrality_measure_names[best_cluster_index]
# Plot the silhouette scores
plt.figure(figsize=(10, 5))
sns.lineplot(x=cluster_counts, y=silhouette_scores, marker='o', linestyle='-')
plt.title('Silhouette Scores for Different Cluster Counts')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')

# Highlight the best cluster count
plt.axvline(x=best_cluster_count, color='red', linestyle='--', label='Best Cluster Count')

# Annotate the best cluster count
plt.annotate(f'Best Cluster Count: {best_cluster_count}\nBest Centrality Measure: {best_centrality_measure_name}',
             xy=(best_cluster_count, max(silhouette_scores)),
             xytext=(best_cluster_count + 1, max(silhouette_scores) - 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.legend()
plt.grid(True)

plt.savefig("figures/optimal cluster.png", dpi=300, bbox_inches='tight')

plt.show()

kmeans = KMeans(n_clusters=best_cluster_count,n_init=10)
cluster_labels = kmeans.fit_predict(covid_scaled)
covid_scaled['Cluster'] = cluster_labels

covid_scaled.to_csv('outputs/corona_cluster_analysis.csv',index=False)

# covid_scaled
print(silhouette_scores)
covid_scaled
