import networkx as nx

edges = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]

G = nx.DiGraph(edges)

print("Ciclos em G:",list(nx.simple_cycles(G)))

+
