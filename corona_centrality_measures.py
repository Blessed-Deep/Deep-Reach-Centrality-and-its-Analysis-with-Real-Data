import networkx as nx
import pandas as pd


corona_edge_data = pd.read_csv("datasets/corona_edges.csv"  )

G = nx.Graph().to_undirected()

edges = list(zip(corona_edge_data["V1"], corona_edge_data["V2"]))
G.add_edges_from(edges)


# Calculate centrality measures

closeness_centrality = nx.closeness_centrality(G)
harmonic_centrality = nx.harmonic_centrality(G)
degree_centrality = nx.degree_centrality(G)

# Decay Centrality
delta = 0.5  # You can adjust this parameter as needed
decay_centrality = {}
for node in G.nodes:
    decay_values = [delta ** dist for dist in nx.shortest_path_length(G, source=node).values()]
    decay_centrality[node] = sum(decay_values)

eccentricity = nx.eccentricity(G)

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

radiality_centrality = calculate_radiality_centrality(G)

load_centrality=nx.load_centrality(G)

approximate_current_flow_betweenness_centrality=nx.approximate_current_flow_betweenness_centrality(G)

betweenness_centrality = nx.betweenness_centrality(G)

current_flow_closeness_centrality=nx.current_flow_closeness_centrality(G)

information_centrality=nx.information_centrality(G)

current_flow_betweenness_centrality=nx.current_flow_betweenness_centrality(G)

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
reach_centrality = reach_centrality(G)

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

deep_reach_centrality = deep_reach_centrality(G)

# Store each centrality function in separate Excel files, sorted by centrality values

centrality_functions = {

    "closeness_centrality": closeness_centrality,
    "harmonic_centrality": harmonic_centrality,
    "degree_centrality": degree_centrality,
    "decay_centrality": decay_centrality,
    "eccentricity": eccentricity,
    "radiality_centrality":radiality_centrality,
    "load_centrality": load_centrality,
    "approximate_current_flow_betweenness_centrality": approximate_current_flow_betweenness_centrality,
    "betweenness_centrality": betweenness_centrality,
    "current_flow_closeness_centrality": current_flow_closeness_centrality,
    "information_centrality": information_centrality,
    "current_flow_betweenness_centrality": current_flow_betweenness_centrality,
    "reach_centrality": reach_centrality,
    "deep_reach_centrality": deep_reach_centrality
}

for centrality_name, centrality_data in centrality_functions.items():
    sorted_data = sorted(centrality_data.items(), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(sorted_data, columns=["Node", centrality_name])
    excel_file_name = f"{centrality_name}.xlsx"
    excel_file_path = "outputs/centrality_measures/" + excel_file_name
    df.to_excel(excel_file_path, index=False)
    print(f"{centrality_name} data saved as {excel_file_name}")



