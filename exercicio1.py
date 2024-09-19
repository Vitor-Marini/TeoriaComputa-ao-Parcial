import networkx as nx

G = nx.Graph()

#nós
G.add_node("1")
G.add_node("2")
G.add_node("3")

#arestas
G.add_edge("1","2")
G.add_edge("1","3")
G.add_edge("2","3")


print("Grafo direcionado G:",G)



import matplotlib.pyplot as plt


fig, ax = plt.subplots()

pos = nx.kamada_kawai_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)

nx.draw_networkx_edges(G, pos, edge_color='gray',width=3)

nx.draw_networkx_labels(G, pos, font_size=15)

plt.axis('off')
plt.show()
