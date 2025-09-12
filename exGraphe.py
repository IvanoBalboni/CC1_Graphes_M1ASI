import networkx as nx
from networkx.utils import py_random_state
import random
import matplotlib.pyplot as plt

def affiche_info(graph):
    print('Noeuds : %s\nAretes : %s' %(graph.nodes,graph.edges))    
    print("Nombre d'arêtes : %s\tNombre de noeuds : %s" %(graph.number_of_edges(),graph.number_of_nodes()))
    print('Graph adjacent nodes : %s'%graph.adj)


def exemplesInstancesPositives(n):
    """ Fonction qui engendre deux graphes aléatoires Galea et Halea
    où Halea est une copie de Galea """
    k = 2*n//3
    prob = .5
    
    Galea = nx.gnp_random_graph(n, prob)

    phi = []
    cible = list(range(n))
    for i in range(k):
        a = random.choice(cible)
        cible.remove(a)
        phi.append(a)

    flag = True
    while flag:
        edges = []
        for x in range(k-1):
            for y in range(x+1,k):
                if (phi[x],phi[y]) in Galea.edges:
                    edges.append((x,y))
        Halea = nx.Graph(edges)
        flag = not nx.is_connected(Halea)

    return Galea, Halea



    
if __name__=='__main__':
    Gex = nx.Graph([(0,2),(1,2),(1,3),(1,4),(1,5),(2,3),(2,6),(2,7),(3,4),(4,5),(4,6),(5,7),(6,7)])
    Hex = nx.Graph([(0,1),(0,2),(0,3),(1,5),(2,3),(3,4),(4,5)])
    affiche_info(Gex)
    # fig = plt.figure(figsize=(20,10))
    # plt.subplot(121)
    # nx.draw(Gex, with_labels=True)
    # plt.subplot(122)
    # nx.draw(Hex, with_labels=True)
    # plt.show()

    Galea, Halea = exemplesInstancesPositives(14)
