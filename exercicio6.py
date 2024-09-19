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

print("Grafo antes da remoçao:",G)

G.remove_node("3")
G.remove_edge("1", "2")

print("\nGrafo depois da remoçao:",G)
