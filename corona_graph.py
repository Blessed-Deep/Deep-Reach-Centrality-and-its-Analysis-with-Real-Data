import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

file_path = "datasets/corona_edges.csv"
data = pd.read_csv(file_path)

G = nx.Graph()

for index, row in data.iterrows():
    node1 = row["V1"]
    node2 = row["V2"]
    G.add_edge(node1, node2)

fig, ax = plt.subplots(figsize=(10, 8))

nx.draw(G, with_labels=True, node_size=20, font_size=2, ax=ax)
plt.title('Corona Graph')
plt.savefig("figures/corona_graph.png", dpi=300, bbox_inches='tight')

plt.show()
