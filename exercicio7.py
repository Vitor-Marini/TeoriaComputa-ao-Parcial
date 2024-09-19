import networkx as nx

G = nx.Graph()

#nós
G.add_node("1")
G.add_node("2")
G.add_node("3")

#arestas
G.add_edge("1","3")
G.add_edge("2","3")

print("Caminho mais curto do nó 1 para o 2", nx.shortest_path(G,source="1" , target="2"))




#print("Vizinhos do nó 1 grafo G:" ,list(G.neighbors("1")))




#print("Grau do nó 1 do grafo G:",G.degree("1"))


#print("Numero de nós do Grafo G:", nx.number_of_nodes(G))
#print("Numero de arestas do Grafo G:", nx.number_of_edges(G))
