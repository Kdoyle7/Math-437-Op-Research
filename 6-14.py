import networkx as nx
import math
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_weighted_edges_from([
    (1, 2, -math.log10(0.8)),
    (1, 4, -math.log10(0.65)),
    (1, 3, -math.log10(0.3)),
    (2, 5, -math.log10(0.5)),
    (2, 4, -math.log10(0.9)),
    (4, 3, -math.log10(0.85)),
    (4, 5, -math.log10(0.7)),
    (4, 6, -math.log10(0.6)),
    (3, 6, -math.log10(0.95)),
    (5, 6, -math.log10(0.5)),
    (5, 7, -math.log10(0.8)),
    (6, 7, -math.log10(0.9))
])

path = nx.shortest_path(G, 1, 7, weight="weight")
length = nx.shortest_path_length(G, 1, 7, weight="weight")

probability = math.pow(10, -length)

print(f"{path=}")
print(f"{length=:.4f}")
print(f"{probability=:.4f}")


pos = nx.spring_layout(G, seed=6)
nx.draw(G, pos, with_labels=True, node_color="thistle", edge_color="red", node_size=700, font_weight="bold")
edge_labels = {k: round(v, 5) for k, v in nx.get_edge_attributes(G, "weight").items()}


nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()