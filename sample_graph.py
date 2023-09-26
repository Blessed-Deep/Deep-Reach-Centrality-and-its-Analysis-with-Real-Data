import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

nodes1 = ['a','b','c','d','e','f','g','h','i','j','k','l']
edges1 = [('d','b'),('c','b'),('a','b'),('b','e'),('e','f'),('f','g'),('f','j'),('g','h'),('j','k'),('h','i'),('k','l')]

EG1 = nx.Graph()

EG1.add_nodes_from(nodes1)
EG1.add_edges_from(edges1)

plt.title("Sample Graph")

pos = nx.spring_layout(EG1)  
nx.draw(EG1, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold', width=2)

# # Save the combined image
combined_filename = "sample_graph/sample_graph.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')

plt.show()
# Centrality Measures ----------------------------

def reach_centrality(G):
    from collections import Counter
    import networkx as nx
    shortest_path_lengths = dict(nx.shortest_path_length(G))
    centrality = dict()
    for x in shortest_path_lengths.values():
        lst = list(x.values())
        key = list(x.keys())
        filtered_values = [x for x in lst if x != 0]
        value_counts = Counter(filtered_values)
        rc = 1
        for value, count in value_counts.items():
            rc = rc + (count/value)
        centrality[key[0]] = rc
    return centrality

rc = reach_centrality(EG1)


def deep_reach_centrality(G):
    import networkx as nx
    shortest_path_lengths = dict(nx.shortest_path_length(G))
    centrality = dict()
    for x in shortest_path_lengths.values():
        key = list(x.keys())
        drc = 0
        for k,v in x.items():
            d = nx.degree(G,k)
            if v!=0 and d!=0:
                drc = drc + (d/v)
        centrality[key[0]] = drc
    return centrality

drc = deep_reach_centrality(EG1)

clo = nx.closeness_centrality(EG1)
har = nx.harmonic_centrality(EG1)
deg = nx.degree_centrality(EG1)

# Decay Centrality
delta = 0.5  # You can adjust this parameter as needed
dec = {}
for node in EG1.nodes:
    decay_values = [delta ** dist for dist in nx.shortest_path_length(EG1, source=node).values()]
    dec[node] = sum(decay_values)

ecc = nx.eccentricity(EG1)

# Radiality centrality
def calculate_radiality_centrality(graph):
    n = len(graph.nodes)
    diam = nx.diameter(graph)
    radiality_centrality = {}
    for u in graph.nodes:
        total_distance = 0
        for w in graph.nodes:
            if u != w:
                total_distance += (diam + 1 - nx.shortest_path_length(graph, source=u, target=w))
        radiality_centrality[u] = total_distance / (n - 1)
    return radiality_centrality

rad = calculate_radiality_centrality(EG1)

load=nx.load_centrality(EG1)

acfb=nx.approximate_current_flow_betweenness_centrality(EG1)

bet = nx.betweenness_centrality(EG1)

cfc=nx.current_flow_closeness_centrality(EG1)

inf=nx.information_centrality(EG1)

cfb=nx.current_flow_betweenness_centrality(EG1)


# Store each centrality function in separate Excel files, sorted by centrality values

centrality_functions = {
     "reach_centrality": rc,
    "deep_reach_centrality": drc,
    "closeness_centrality": clo,
    "harmonic_centrality": har,
    "degree_centrality": deg,
    "decay_centrality": dec,
    "eccentricity": ecc,
    "radiality_centrality":rad,
    "load_centrality": load,
    "approximate_current_flow_betweenness_centrality": acfb,
    "betweenness_centrality": bet,
    "current_flow_closeness_centrality": cfc,
    "information_centrality": inf,
    "current_flow_betweenness_centrality": cfb
   
}

# Save the outputs

for centrality_name, centrality_data in centrality_functions.items():
    df = pd.DataFrame(centrality_data.items(), columns=["Node", centrality_name])
    excel_file_name = f"{centrality_name}.xlsx"
    excel_file_path = "sample_graph/centrality_measures/" + excel_file_name
    df.to_excel(excel_file_path, index=False)
    print(f"{centrality_name} data saved to {excel_file_name}")

    
    