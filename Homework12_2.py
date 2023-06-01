print ("EXERCISE 12.2")
print ("The graph open in a new window in a moment")
import networkx as nx
import matplotlib.pyplot as plt
import random

def random_graph(n):
    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))
    
    for i in range(1, n + 1):
        num_edges = random.randint(1, 3)
        existing_edges = set(G.neighbors(i))
        
        for _ in range(num_edges):
            neighbors = set(range(1, n + 1)) - existing_edges - {i}
            
            if not neighbors:
                break
            
            new_neighbor = random.choice(list(neighbors))
            G.add_edge(i, new_neighbor)
            existing_edges.add(new_neighbor)

    return G

G = random_graph(10)

nx.draw(G, with_labels=True, node_color='lightgreen', edge_color='darkgray')
plt.show()
