import networkx as nx 

filename = "file25.txt"

with open(filename) as file:
    data = file.read().splitlines()
    
t = {line.split(":")[0]: line.split()[1:] for line in data}
g = nx.Graph(t)
g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)
print(len(a) * len(b))
