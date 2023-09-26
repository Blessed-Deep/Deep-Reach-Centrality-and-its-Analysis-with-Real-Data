import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

all_silhouette_widths = pd.read_csv('outputs/all_silhouette_widths.csv')

all_sw = pd.DataFrame({'silhouette_widths':all_silhouette_widths['silhouette_widths']})

average_silhouette_width = sum(all_silhouette_widths['silhouette_widths']) / len(all_silhouette_widths['silhouette_widths'])
print("Average Silhouette Width:", average_silhouette_width)


for k in range(2,11):
    kmeans = KMeans(n_clusters=k,  random_state=0, n_init = 10) # n_init = 10 to supress warning
    cluster_labels = kmeans.fit_predict(all_sw)
    all_silhouette_widths['Cluster'] = cluster_labels

    
all_silhouette_widths = all_silhouette_widths.sort_values(by=['Cluster'])

x1_length = len(all_silhouette_widths)

legend_labels = {
    'Cluster 9': '#17becf',
    'Cluster 8': '#bcbd22',
    'Cluster 7': '#7f7f7f',
    'Cluster 6': '#e377c2',
    'Cluster 5': '#8c564b',
    'Cluster 4': '#9467bd',
    'Cluster 3': '#d62728',
    'Cluster 2': '#2ca02c',
    'Cluster 1': '#ff7f0e',
    'Cluster 0': '#1f77b4'
}

single_digit_mapping = {
    0: 'Cluster 0',
    1: 'Cluster 1',
    2: 'Cluster 2',
    3: 'Cluster 3',
    4: 'Cluster 4',
    5: 'Cluster 5',
    6: 'Cluster 6',
    7: 'Cluster 7',
    8: 'Cluster 8',
    9: 'Cluster 9'
}
all_silhouette_widths['Legend'] = all_silhouette_widths['Cluster'].map(single_digit_mapping)
all_silhouette_widths['bar_color'] = all_silhouette_widths['Legend'].map(legend_labels)


fig = px.bar(all_silhouette_widths, x='centrality', y='silhouette_widths', color=all_silhouette_widths['Legend'],
             title='Silhouette plot, average silhouette width: 0.829',
#              text = all_silhouette_widths['silhouette_widths'],
             labels={'centrality': '', 'Silhouette_Width': 'Silhouette Width', 'Cluster': 'Clusters'},
             category_orders={'Cluster': [f'Cluster_{k}' for k in range(2, 11)]})

fig.add_shape(type='line', x0=-0.5, x1=x1_length,
              y0=average_silhouette_width, y1=average_silhouette_width,
              line=dict(color='red', width=2, dash='dash'),
              name='Average Silhouette Width')
fig.update_xaxes(tickangle=90)  # Rotate x-axis labels for better visibility


fig.update_layout(
    width=800,  
    height=600,
    showlegend=True,  
    legend_title_text='Clusters'
)

fig.write_image("figures/clusters_in_centrality_functions.png", engine="kaleido")

fig.show()

all_silhouette_widths
