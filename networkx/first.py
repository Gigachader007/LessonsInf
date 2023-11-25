import networkx as nx
import matplotlib.pyplot as plt
import random
import string

graph = nx.Graph()

nodes = []
while len(nodes) < 10:
    t = random.choice(string.ascii_letters)
    if t not in nodes:
        nodes.append(t)
        graph.add_node(t)

for i in range(30):
    graph.add_edge(random.choice(nodes),random.choice(nodes),weight=random.randint(-100,100))

pos = nx.circular_layout(graph)
nx.draw(graph,pos,with_labels=True,font_weight='bold')
edge_weight = nx.get_edge_attributes(graph,'weight')
nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_weight)
plt.show()
