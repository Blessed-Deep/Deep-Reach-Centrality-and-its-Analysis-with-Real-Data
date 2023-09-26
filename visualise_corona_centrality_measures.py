import pandas as pd
import matplotlib.pyplot as plt

# Load node labels for COVID and H1N1
corona_node_labels = pd.read_excel("datasets/corona_nodes.xlsx")

# Load centrality data for the two graphs and centrality measures
closeness_centrality = pd.read_excel("outputs/centrality_measures/closeness_centrality.xlsx")
harmonic_centrality = pd.read_excel("outputs/centrality_measures/harmonic_centrality.xlsx")
degree_centrality = pd.read_excel("outputs/centrality_measures/degree_centrality.xlsx")
decay_centrality = pd.read_excel("outputs/centrality_measures/decay_centrality.xlsx")
eccentricity = pd.read_excel("outputs/centrality_measures/eccentricity.xlsx")
radiality_centrality = pd.read_excel("outputs/centrality_measures/radiality_centrality.xlsx")
load_centrality = pd.read_excel("outputs/centrality_measures/load_centrality.xlsx")
approximate_current_flow_betweenness_centrality = pd.read_excel("outputs/centrality_measures/approximate_current_flow_betweenness_centrality.xlsx")
betweenness_centrality = pd.read_excel("outputs/centrality_measures/betweenness_centrality.xlsx")
current_flow_closeness_centrality = pd.read_excel("outputs/centrality_measures/current_flow_closeness_centrality.xlsx")
information_centrality = pd.read_excel("outputs/centrality_measures/information_centrality.xlsx")
current_flow_betweenness_centrality = pd.read_excel("outputs/centrality_measures/current_flow_betweenness_centrality.xlsx")
reach_centrality = pd.read_excel("outputs/centrality_measures/reach_centrality.xlsx")
deep_reach_centrality = pd.read_excel("outputs/centrality_measures/deep_reach_centrality.xlsx")

# Merge node labels with centrality data
closeness_centrality = closeness_centrality.merge(corona_node_labels, on='Node')
harmonic_centrality = harmonic_centrality.merge(corona_node_labels, on='Node')
degree_centrality = degree_centrality.merge(corona_node_labels, on='Node')
decay_centrality = decay_centrality.merge(corona_node_labels, on='Node')
eccentricity = eccentricity.merge(corona_node_labels, on='Node')
radiality_centrality =radiality_centrality.merge(corona_node_labels, on='Node')
load_centrality = load_centrality.merge(corona_node_labels, on='Node')
approximate_current_flow_betweenness_centrality = approximate_current_flow_betweenness_centrality.merge(corona_node_labels, on='Node')

betweenness_centrality = betweenness_centrality.merge(corona_node_labels, on='Node')
current_flow_closeness_centrality = current_flow_closeness_centrality.merge(corona_node_labels, on='Node')
information_centrality = information_centrality.merge(corona_node_labels, on='Node')
current_flow_betweenness_centrality = current_flow_betweenness_centrality.merge(corona_node_labels, on='Node')
reach_centrality = reach_centrality.merge(corona_node_labels, on='Node')
deep_reach_centrality = deep_reach_centrality.merge(corona_node_labels, on='Node')


# Choose the top number of nodes to visualize
num_top_nodes = 25

# Create subplots for each centrality measure
plt.figure(figsize=(25, 30))

# Closeness
plt.subplot(5, 3, 1)
top_nodes_closeness_centrality = closeness_centrality.nlargest(num_top_nodes, 'closeness_centrality')
plt.scatter(top_nodes_closeness_centrality['corona_nodes'], top_nodes_closeness_centrality['closeness_centrality'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Closeness',fontsize=20)
plt.xticks(rotation=45)

# Harmonic
plt.subplot(5, 3, 2)
top_nodes_harmonic_centrality = harmonic_centrality.nlargest(num_top_nodes, 'harmonic_centrality')
plt.scatter(top_nodes_harmonic_centrality['corona_nodes'], top_nodes_harmonic_centrality['harmonic_centrality'], color='green')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Harmonic',fontsize=20)
plt.xticks(rotation=45)

# Degree
plt.subplot(5, 3, 3)
top_nodes_degree_centrality = degree_centrality.nlargest(num_top_nodes, 'degree_centrality')
plt.scatter(top_nodes_degree_centrality['corona_nodes'], top_nodes_degree_centrality['degree_centrality'], color='blue')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Degree',fontsize=20)
plt.xticks(rotation=45)

# Decay
plt.subplot(5, 3, 4)
top_nodes_decay_centrality = decay_centrality.nlargest(num_top_nodes, 'decay_centrality')
plt.scatter(top_nodes_decay_centrality['corona_nodes'], top_nodes_decay_centrality['decay_centrality'], color='black')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Decay',fontsize=20)
plt.xticks(rotation=45)

# Eccentricity
plt.subplot(5, 3, 5)
top_nodes_eccentricity = eccentricity.nlargest(num_top_nodes, 'eccentricity')
plt.scatter(top_nodes_eccentricity['corona_nodes'], top_nodes_eccentricity['eccentricity'], color='purple')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Eccentricity',fontsize=20)
plt.xticks(rotation=45)

# Radiality
plt.subplot(5, 3, 6)
top_nodes_radiality_centrality = radiality_centrality.nlargest(num_top_nodes, 'radiality_centrality')
plt.scatter(top_nodes_radiality_centrality['corona_nodes'], top_nodes_radiality_centrality['radiality_centrality'], color='brown')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Radiality',fontsize=20)
plt.xticks(rotation=45)

# load
plt.subplot(5, 3, 7)
top_nodes_load_centrality = load_centrality.nlargest(num_top_nodes, 'load_centrality')
plt.scatter(top_nodes_load_centrality['corona_nodes'], top_nodes_load_centrality['load_centrality'], color='gray')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Load',fontsize=20)
plt.xticks(rotation=45)

# Approximate Current Flow Betweenness
plt.subplot(5, 3, 8)
top_nodes_approximate_current_flow_betweenness_centrality = approximate_current_flow_betweenness_centrality.nlargest(num_top_nodes, 'approximate_current_flow_betweenness_centrality')
plt.scatter(top_nodes_approximate_current_flow_betweenness_centrality['corona_nodes'], top_nodes_approximate_current_flow_betweenness_centrality['approximate_current_flow_betweenness_centrality'], color='magenta')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Approx Current Flow Betweenness',fontsize=20)
plt.xticks(rotation=45)

# --------------
# Betweenness
plt.subplot(5, 3, 9)
top_nodes_betweenness_centrality = betweenness_centrality.nlargest(num_top_nodes, 'betweenness_centrality')
plt.scatter(top_nodes_betweenness_centrality['corona_nodes'], top_nodes_betweenness_centrality['betweenness_centrality'], color='blue')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Betweenness',fontsize=20)
plt.xticks(rotation=45)

# Current Flow Closeness
plt.subplot(5, 3, 10)
top_nodes_current_flow_closeness_centrality = current_flow_closeness_centrality.nlargest(num_top_nodes, 'current_flow_closeness_centrality')
plt.scatter(top_nodes_current_flow_closeness_centrality['corona_nodes'], top_nodes_current_flow_closeness_centrality['current_flow_closeness_centrality'], color='black')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Current Flow Closeness',fontsize=20)
plt.xticks(rotation=45)

# Information
plt.subplot(5, 3, 11)
top_nodes_information_centrality = information_centrality.nlargest(num_top_nodes, 'information_centrality')
plt.scatter(top_nodes_information_centrality['corona_nodes'], top_nodes_information_centrality['information_centrality'], color='purple')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Information',fontsize=20)
plt.xticks(rotation=45)

# Current Flow Betweenness
plt.subplot(5, 3, 12)
top_nodes_current_flow_betweenness_centrality = current_flow_betweenness_centrality.nlargest(num_top_nodes, 'current_flow_betweenness_centrality')
plt.scatter(top_nodes_current_flow_betweenness_centrality['corona_nodes'], top_nodes_current_flow_betweenness_centrality['current_flow_betweenness_centrality'], color='brown')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Current Flow Betweenness',fontsize=20)
plt.xticks(rotation=45)

# Reach
plt.subplot(5, 3, 13)
top_nodes_reach_centrality = reach_centrality.nlargest(num_top_nodes, 'reach_centrality')
plt.scatter(top_nodes_reach_centrality['corona_nodes'], top_nodes_reach_centrality['reach_centrality'], color='magenta')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Reach',fontsize=20)
plt.xticks(rotation=45)

# Deep Reach
plt.subplot(5, 3, 14)
top_nodes_deep_reach_centrality = deep_reach_centrality.nlargest(num_top_nodes, 'deep_reach_centrality')
plt.scatter(top_nodes_deep_reach_centrality['corona_nodes'], top_nodes_deep_reach_centrality['deep_reach_centrality'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Deep Reach',fontsize=20)
plt.xticks(rotation=45)
plt.tick_params(axis='y', labelsize=15)



plt.tight_layout()

# # Save the combined image
combined_filename = "figures/centrality_measures.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.show()