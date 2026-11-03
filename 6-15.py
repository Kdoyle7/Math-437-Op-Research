import networkx as nx


G = nx.DiGraph()

G.add_weighted_edges_from([
    (1, 2, 1700),
    (1, 3, 3968),
    (1, 4, 7622),
    (1, 5, 10970),
    (2, 3, 1880),
    (2, 4, 4652),
    (2, 5, 7244),
    (3, 4, 2300),
    (3, 5, 4316),
    (4, 5, 2720)
])

path = nx.shortest_path(G, 1, 5, weight="weight")
length = nx.shortest_path_length(G, 1, 5, weight="weight")

print(path, length)