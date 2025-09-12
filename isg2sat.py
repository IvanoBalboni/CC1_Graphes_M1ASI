import networkx as nx                                                   

class Reduction(object):
    def __init__(self,grG,grH):
        self.g = grG
        self.h = grH
        self.n = grG.number_of_nodes()
        self.k = grH.number_of_nodes()
        self.toutes_les_clauses = self.clauses_a() + self.clauses_b() # + self.clauses_c() + self.clauses_d()

    def code(self,i,j): # p(0,0) -> 1 ...
        return i*self.k+j+1
 
    def clauses_a(self):  # au moins un 'vrai' sur chaque colonne
        return [[self.code(i,j) for i in range(self.n)] for j in range(self.k)]

    def clauses_b(self):  # au plus un 'vrai' sur chaque colonne
        clauses = []
        for j in range(self.k):
            for a in range(self.n-1):
                for b in range(1+a,self.n):            
                    clauses.append([-self.code(a,j),-self.code(b,j)])
        return clauses



 
    
if __name__=='__main__':
    G3 = nx.Graph([(0,1),(1,2),(1,3),(2,3)])
    H3 = nx.Graph([(0,1), (0,2) ,(1,2)])

    c = Reduction(G3,H3)
   
    print("%s\n" %c.toutes_les_clauses)
 
 
