#kruskal's algorithm

import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=5)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=3)

minimum_spanning_tree = nx.minimum_spanning_tree(G)

for edge in minimum_spanning_tree.edges(data=True):
    print(edge)
