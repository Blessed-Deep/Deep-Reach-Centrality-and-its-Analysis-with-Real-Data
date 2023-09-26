import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
corona_scaled = pd.read_excel("outputs/centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")

corona_scaled = corona_scaled.drop(['Node', 'corona_nodes'], axis=1)

corona_correlation = corona_scaled.corr()


# Plot the corona correlation
plt.title('Corona Correlation',fontweight='bold')
sns.heatmap(corona_correlation, annot=False, cmap='coolwarm', linewidths=0)


combined_filename = "figures/dissimilarity_matrix_for_corona.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')


plt.show()