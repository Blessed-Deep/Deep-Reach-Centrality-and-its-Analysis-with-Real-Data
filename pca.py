import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

covid_scaled = pd.read_excel("outputs/centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")

covid_scaled = covid_scaled.drop(['Node', 'corona_nodes'], axis=1)

Functions = covid_scaled.columns.tolist()

Functions = [func.replace('_centrality', '') for func in Functions]
index_to_update = Functions.index('approximate_current_flow_betweenness')

Functions[index_to_update] = 'approx_current_flow_betweenness'

pca_covid = PCA()

pca_covid.fit(covid_scaled)

pca_components_covid = pca_covid.components_[0]

visualization_df = pd.DataFrame({
    'Centrality Measure': Functions,
    'PCA Component (Corona)': pca_components_covid
})
cluster_analysis=visualization_df
visualization_df = visualization_df.sort_values(by='PCA Component (Corona)',ascending=False)

plt.figure(figsize=(10, 5))
ax = sns.heatmap(data=visualization_df.set_index('Centrality Measure').T, cmap='coolwarm', annot=True,
                 fmt=".2f", cbar=False, annot_kws={"rotation": 90})
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Reset xticklabels to horizontal
plt.title('PCA Components for Centrality Measures')

plt.savefig("figures/pca.png", dpi=300, bbox_inches='tight')
cluster_analysis.to_csv('outputs/pca.csv',index=False)

plt.show()
