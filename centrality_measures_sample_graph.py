import pandas as pd
import matplotlib.pyplot as plt


# Load centrality data for the two graphs and centrality measures
reach_centrality = pd.read_excel("sample_graph/centrality_measures/reach_centrality.xlsx")
deep_reach_centrality = pd.read_excel("sample_graph/centrality_measures/deep_reach_centrality.xlsx")
closeness_centrality = pd.read_excel("sample_graph/centrality_measures/closeness_centrality.xlsx")
harmonic_centrality = pd.read_excel("sample_graph/centrality_measures/harmonic_centrality.xlsx")
degree_centrality = pd.read_excel("sample_graph/centrality_measures/degree_centrality.xlsx")
decay_centrality = pd.read_excel("sample_graph/centrality_measures/decay_centrality.xlsx")
eccentricity = pd.read_excel("sample_graph/centrality_measures/eccentricity.xlsx")
radiality_centrality = pd.read_excel("sample_graph/centrality_measures/radiality_centrality.xlsx")
load_centrality = pd.read_excel("sample_graph/centrality_measures/load_centrality.xlsx")
approximate_current_flow_betweenness_centrality = pd.read_excel("sample_graph/centrality_measures/approximate_current_flow_betweenness_centrality.xlsx")
betweenness_centrality = pd.read_excel("sample_graph/centrality_measures/betweenness_centrality.xlsx")
current_flow_closeness_centrality = pd.read_excel("sample_graph/centrality_measures/current_flow_closeness_centrality.xlsx")
information_centrality = pd.read_excel("sample_graph/centrality_measures/information_centrality.xlsx")
current_flow_betweenness_centrality = pd.read_excel("sample_graph/centrality_measures/current_flow_betweenness_centrality.xlsx")


# Create subplots for each centrality measure
plt.figure(figsize=(25, 20))

# Reach
plt.subplot(4, 4, 1)
plt.scatter(reach_centrality['Node'], reach_centrality['reach_centrality'], s=100, color='magenta')
plt.ylabel('Centrality Value')
plt.title('Reach',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Deep Reach
plt.subplot(4, 4, 2)
plt.scatter(deep_reach_centrality['Node'], deep_reach_centrality['deep_reach_centrality'], s=100, color='red')
plt.ylabel('Centrality Value')
plt.title('Deep Reach',fontsize=20)
plt.xticks(rotation=0, fontsize=20)
plt.tick_params(axis='y', labelsize=15)

# Closeness
plt.subplot(4, 4, 3)
plt.scatter(closeness_centrality['Node'], closeness_centrality['closeness_centrality'], s=100, color='red')
plt.ylabel('Centrality Value')
plt.title('Closeness',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Harmonic
plt.subplot(4, 4, 4)
plt.scatter(harmonic_centrality['Node'], harmonic_centrality['harmonic_centrality'], s=100, color='green')
plt.ylabel('Centrality Value')
plt.title('Harmonic',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Degree
plt.subplot(4, 4, 5)
plt.scatter(degree_centrality['Node'], degree_centrality['degree_centrality'], s=100, color='blue')
plt.ylabel('Centrality Value')
plt.title('Degree',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Decay
plt.subplot(4, 4, 6)
plt.scatter(decay_centrality['Node'], decay_centrality['decay_centrality'], s=100, color='black')
plt.ylabel('Centrality Value')
plt.title('Decay',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Eccentricity
plt.subplot(4, 4, 7)
plt.scatter(eccentricity['Node'], eccentricity['eccentricity'], s=100, color='purple')
plt.ylabel('Centrality Value')
plt.title('Eccentricity',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Radiality
plt.subplot(4, 4, 8)
plt.scatter(radiality_centrality['Node'], radiality_centrality['radiality_centrality'], s=100, color='brown')
plt.ylabel('Centrality Value')
plt.title('Radiality',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# load
plt.subplot(4, 4, 9)
plt.scatter(load_centrality['Node'], load_centrality['load_centrality'], s=100, color='gray')
plt.ylabel('Centrality Value')
plt.title('Load',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Approximate Current Flow Betweenness
plt.subplot(4, 4, 10)
plt.scatter(approximate_current_flow_betweenness_centrality['Node'], approximate_current_flow_betweenness_centrality['approximate_current_flow_betweenness_centrality'], s=100, color='magenta')
plt.ylabel('Centrality Value')
plt.title('Approx Current Flow Betweenness',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# --------------
# Betweenness
plt.subplot(4, 4, 11)
plt.scatter(betweenness_centrality['Node'], betweenness_centrality['betweenness_centrality'], s=100, color='blue')
plt.title('Betweenness',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Current Flow Closeness
plt.subplot(4, 4, 12)
plt.scatter(current_flow_closeness_centrality['Node'], current_flow_closeness_centrality['current_flow_closeness_centrality'], s=100, color='black')
plt.ylabel('Centrality Value')
plt.title('Current Flow Closeness',fontsize=20)
plt.xticks(rotation=0, fontsize=20)

# Information
plt.subplot(4, 4, 13)
plt.scatter(information_centrality['Node'], information_centrality['information_centrality'], s=100, color='purple')
plt.ylabel('Centrality Value')
plt.title('Information',fontsize=20)

# Current Flow Betweenness
plt.subplot(4, 4, 14)
plt.scatter(current_flow_betweenness_centrality['Node'], current_flow_betweenness_centrality['current_flow_betweenness_centrality'], s=100, color='brown')
plt.ylabel('Centrality Value')
plt.title('Current Flow Betweenness',fontsize=20)





plt.tight_layout()

# # Save the combined image
combined_filename = "sample_graph/centrality_measures.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.show()