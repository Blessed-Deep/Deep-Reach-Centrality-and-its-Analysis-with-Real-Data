import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

# Load your scaled data and drop unnecessary columns
covid_scaled = pd.read_excel("outputs/centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")
covid_scaled = covid_scaled.drop(['Node', 'corona_nodes'], axis=1)

Functions = covid_scaled.columns.tolist()

Functions = [func.replace('_centrality', '') for func in Functions]
index_to_update = Functions.index('approximate_current_flow_betweenness')

Functions[index_to_update] = 'approx_current_flow_betweenness'
covid_scaled.columns = Functions

# Initialize an empty list to store silhouette widths
silhouette_widths = []


# Iterate through columns and calculate silhouette widths
for column in covid_scaled.columns:
    # Perform K-means clustering 
    # Here we are taking optimal cluster number k=2 because we already defined using silhouette method
    kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
    cluster_labels = kmeans.fit_predict(covid_scaled[column].values.reshape(-1, 1))
    # Calculate silhouette score
    silhouette_avg = silhouette_score(covid_scaled[column].values.reshape(-1, 1), cluster_labels)
    silhouette_widths.append(silhouette_avg)

average_silhouette_width = sum(silhouette_widths) / len(silhouette_widths)
print("Average Silhouette Width:", average_silhouette_width)

# Create a bar plot for silhouette widths
plt.figure(figsize=(12, 8))
plt.bar(covid_scaled.columns, silhouette_widths)
# Add a horizontal line for the average silhouette width
plt.axhline(y=average_silhouette_width, color='red', linestyle='--', label='Average Silhouette Width')
# plt.xlabel('SARS-CoV-2',fontsize=20)
plt.ylabel('Silhouette Width')
plt.title('SARS-CoV-2 Silhouette Width for Each Function')
plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
# Show the legend for the average silhouette width
plt.tight_layout()
plt.show()

all_silhouette_widths = pd.DataFrame({'centrality':covid_scaled.columns,
                                      'silhouette_widths':silhouette_widths
                                     })
all_silhouette_widths.to_csv('outputs/all_silhouette_widths.csv',index=False)

all_silhouette_widths