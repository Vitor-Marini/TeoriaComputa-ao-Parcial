import networkx as nx
import matplotlib.pyplot as plt

#Cria um grafo com "n" nós e "p" probabilidade de arestas
G= nx.erdos_renyi_graph(1000, 0.01)


fig, ax = plt.subplots()

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=200)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10)

plt.axis('off')
plt.show()
