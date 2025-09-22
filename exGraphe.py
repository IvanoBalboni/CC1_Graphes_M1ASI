import networkx as nx
from networkx.utils import py_random_state
import random
import matplotlib.pyplot as plt
import itertools as iter
import isg2sat as i2s
import cProfile
import pstats
import io




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

    if len(Galea.edges) <= 15:
        print("problemes possibles")

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

def verifISG(G, H, phi):
    '''
    verifie si pour les graphes G, H, l'injection phi verifie ISO-SOUS-GRAPHES.
    les sommets de G doivent etre une liste triee en ordre croissant dans [0-(n-1)], n le nb de sommets
    '''
    #print("teste G:", G.nodes)
    #print("teste H:", H.nodes)
    #print("teste phi:", phi)

    #range dans un dictionaire les sommets de H en cle et leur position en indice pour l'injection phi
    H_pos = {}
    i = 0
    for node in H.nodes:
        H_pos[node] = i
        i+=1
    
    for (x, y) in H.edges:
        '''
        if x >= len(phi) or y >= len(phi):
            print("G ",G.nodes)
            print("H ",H.nodes)
            print("phi ", phi)
            print("x : ", x, "  y : ", y)
        '''
        if not G.has_edge(phi[H_pos[x]], phi[H_pos[y]]):
            return False

    return True

def forceBruteISG(G, H):
    '''
    execute verifISG pour tout les phi possibles jusqu'a trouver une instance positive (retourne True)
    retourne Faux sinon
    '''
    HLen = len(H.nodes)
    phi_list = list(iter.permutations(range(len(G.nodes)), HLen))
    i = 0
    for phi in phi_list:
        if verifISG(G, H, phi):
            #print(H.nodes)
            #print(phi)
            return True
    return False

    
if __name__=='__main__':
    #instance positive
    Gex = nx.Graph([(0,2),(1,2),(1,3),(1,4),(1,5),(2,3),(2,6),(2,7),(3,4),(4,5),(4,6),(5,7),(6,7)])
    Hex = nx.Graph([(0,1),(0,2),(0,3),(1,5),(2,3),(3,4),(4,5)])

    #instance positive
    G1 = nx.Graph([(0,1),(0,3),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(4,5)])
    H1 = nx.Graph([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])

    #instance negative
    G2 = nx.Graph([(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)])
    H2 = nx.Graph([(0,1),(1,2),(2,3),(0,3),(0,2)])

    #instance positive
    G3 = nx.Graph([(0,1),(1,2),(1,3),(2,3)])
    H3 = nx.Graph([(0,1), (0,2) ,(1,2)])
    #affiche_info(Gex)
    
    Galea1, Halea1 = exemplesInstancesPositives(9)
    Galea2, Halea2 = exemplesInstancesPositives(10)
    Galea3, Halea3 = exemplesInstancesPositives(11)
    Galea4, Halea4 = exemplesInstancesPositives(31)

    #limites avant explosion en duree
    Galea3B, Halea3B = exemplesInstancesPositives(12)
    Galea4B, Halea4B = exemplesInstancesPositives(32)

    #phi = [1,2,3,4,5,7]

    #print( verifISG(G3, H3, [1,2,0]) )
    #print(forceBruteISG(Gex, Hex))
    #print(verifISG(Gex, Hex, phi))


    ### Question 5 ###
    print("### Question 5 ###")
    bm = cProfile.Profile()
    bm.enable()
    
    print("test forceBrute ex: ",forceBruteISG(Gex, Hex))
    print("test forceBrute 1: ",forceBruteISG(G1, H1))
    print("test forceBrute 2: ",forceBruteISG(G2, H2))
    print("test forceBrute 3: ",forceBruteISG(G3, H3))
    print("test forceBrute Gal/Hal 1: ",forceBruteISG(Galea1, Halea1))
    print("test forceBrute Gal/Hal 2: ",forceBruteISG(Galea2, Halea2))
    print("test forceBrute Gal/Hal 3:", forceBruteISG(Galea3, Halea3))
    

    bm.disable()
    s = io.StringIO()
    ps = pstats.Stats(bm, stream=s).sort_stats('cumtime')
    ps.print_stats()

    with open('benchmark_small_bruteForce.txt', 'w+') as f:
        f.write(s.getvalue())
    

    bm = cProfile.Profile()
    bm.enable()

    print("test forceBrute Gal/Hal 3: ",forceBruteISG(Galea3B, Halea3B))

    bm.disable()
    s = io.StringIO()
    ps = pstats.Stats(bm, stream=s).sort_stats('cumtime')
    ps.print_stats()

    with open('benchmark_big_bruteForce.txt', 'w+') as f:
        f.write(s.getvalue())
    
    ### Question 11 ###
    print("### Question 11 ###")
    bm = cProfile.Profile()
    bm.enable()

    print("test isg2sat ex:", i2s.solveurISG(Gex, Hex))
    print("test isg2sat 1:", i2s.solveurISG(G1, H1))
    print("test isg2sat 2:", i2s.solveurISG(G2, H2))
    print("test isg2sat 3:", i2s.solveurISG(G3, H3))
    print("test isg2sat Gal/Hal 1:", i2s.solveurISG(Galea1, Halea1))
    print("test isg2sat Gal/Hal 2:", i2s.solveurISG(Galea2, Halea2))
    print("test isg2sat Gal/Hal 3:", i2s.solveurISG(Galea3, Halea3))
    print("test isg2sat Gal/Hal 3B:", i2s.solveurISG(Galea3B, Halea3B))
    print("test isg2sat Gal/Hal 4:", i2s.solveurISG(Galea4, Halea4))

    bm.disable()
    s = io.StringIO()
    ps = pstats.Stats(bm, stream=s).sort_stats('cumtime')
    ps.print_stats()

    with open('benchmark_small_isg2sat.txt', 'w+') as f:
        f.write(s.getvalue())


    bm = cProfile.Profile()
    bm.enable()
    
    print("test isg2sat Gal/Hal 4B:", i2s.solveurISG(Galea4B, Halea4B))

    bm.disable()
    s = io.StringIO()
    ps = pstats.Stats(bm, stream=s).sort_stats('cumtime')
    ps.print_stats()

    with open('benchmark_big_isg2sat.txt', 'w+') as f:
        f.write(s.getvalue())




    
    