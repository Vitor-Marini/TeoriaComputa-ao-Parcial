import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#path para o dataset
facebook_folder = 'facebook_combined.txt'
#transformando o dataset em um dataframe do pandas
facebook = pd.read_csv(facebook_folder, sep=" ", names=["start_node", "end_node"])

#criando o grafo
G = nx.from_pandas_edgelist(facebook, "start_node", "end_node")

#dados retirados do grafo
print("Numero de Nós:",G.number_of_nodes())
print("Numero de arestas",G.number_of_edges())
print("Grau medio = ",np.mean([d for _, d in G.degree()]))
print("Densidade:",nx.density(G))
print("Clusters(media):",nx.average_clustering(G))
print("Componentes:",nx.number_connected_components(G))


#plot do grafo(nós e arestas)
pos = nx.spring_layout(G, iterations=15, seed=1500)
plt.figure(figsize=(15, 9))
nx.draw(G, pos=pos, node_size=10, with_labels=False, width=0.15,node_color='pink',edge_color='gray')
plt.axis("off")
plt.show()


#plot grafico de coeficiente de agrupamento(cluster)
plt.figure(figsize=(15, 9))
plt.hist(nx.clustering(G).values(), bins=50)
plt.title("Histograma de coeficiente de agrupamento ", fontdict={"size": 35}, loc="center")
plt.xlabel("Coeficiente de agrupamento", fontdict={"size": 20})
plt.ylabel("Conatgem", fontdict={"size": 20})
plt.show()



degree_centrality = nx.centrality.degree_centrality(G)
(sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True))[:8]

#plot histograma de centralidade de grau
plt.figure(figsize=(15, 8))
plt.hist(degree_centrality.values(), bins=25)
plt.xticks(ticks=[0, 0.025, 0.05, 0.1, 0.15, 0.2])  # set the x axis ticks
plt.title("Histograma de centralidade de grau", fontdict={"size": 35}, loc="center")
plt.xlabel("Grau de centralidade", fontdict={"size": 20})
plt.ylabel("Contagem", fontdict={"size": 20})


#detecçao das comunidades e organizaçao para representaçao grafica de cor por comunidade
comunidades = list(nx.community.greedy_modularity_communities(G))

mapa_comunidades = {}
for index_comunidade, comunidade in enumerate(comunidades):
    for no in comunidade:
        mapa_comunidades[no] = index_comunidade

#plot grafo baseado nas comunidades
pos = nx.spring_layout(G, iterations=15, seed=1500)
plt.figure(figsize=(15, 9))
node_colors = [mapa_comunidades[node] for node in G.nodes()]
nx.draw(G, pos=pos, node_size=10, with_labels=False, width=0.15,
        node_color=node_colors,cmap = matplotlib.colormaps.get_cmap("viridis"), edge_color='gray')
plt.axis("off")
plt.show()
