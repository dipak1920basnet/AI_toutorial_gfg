import networkx as nx
import matplotlib.pyplot as plt 

G = nx.Graph() #Undirected Graph
DG = nx.DiGraph() #Directed Graph
MG = nx.MultiGraph() #Multiple edges between nodes
MDG = nx.MultiDiGraph() #Multiple direction in multigraph

G.add_edge(1,2)
G.add_edge(2,3, weight=0.9)

G.add_edge("A","B")
G.add_edge("B","B")

G.add_node("C")
G.add_node(print)

nx.draw_spring(G, with_labels=True)
plt.show()