import networkx as nx

G = nx.DiGraph()

#nós
G.add_node("1")
G.add_node("2")
G.add_node("3")

#arestas
G.add_edge("1","2")
G.add_edge("1","3")
G.add_edge("2","3")

print("Existe aresta entre nó 1 e 2:",G.has_edge("1","2"))




print("Existe o nó 1 no grafo :",G.has_node("1"))
