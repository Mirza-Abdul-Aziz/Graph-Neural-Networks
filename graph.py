import networkx as nx
import matplotlib.pyplot as plt
H = nx.DiGraph()
H.add_nodes_from([
    (0, {"color": "red", "size": 500}),
    (1, {"color": "blue", "size": 500}),
    (2, {"color": "green", "size": 500}),
    (3, {"color": "yellow", "size": 500}),
    (4, {"color": "pink", "size": 500}),
    (5, {"color": "purple", "size": 500})
])

H.add_edges_from([
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (3, 5),
    (4, 5)
])
node_colors = nx.get_node_attributes(H, "color").values()
colors = list(node_colors)
node_sizes = nx.get_node_attributes(H, "size").values()
sizes = list(node_sizes)
nx.draw(H, node_color=colors, node_size=sizes, with_labels=True)
plt.show()