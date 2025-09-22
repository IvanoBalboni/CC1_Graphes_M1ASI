import networkx as nx     
import exSolveur as solve                                         

class Reduction(object):
    def __init__(self,grG,grH):
        self.g = grG
        self.h = grH
        self.n = grG.number_of_nodes()
        self.k = grH.number_of_nodes()
        self.toutes_les_clauses = self.clauses_a() + self.clauses_b() + self.clauses_c() + self.clauses_d()

    def code(self,i,j): # p(0,0) -> 1 ...
        return i*self.k+j+1
    
    def decode(self, ij):
        ij -= 1
        i = ij // self.k
        j = ij % self.k
        return (i, j)

 
    def clauses_a(self):  # au moins un 'vrai' sur chaque colonne
        return [[self.code(i,j) for i in range(self.n)] for j in range(self.k)]

    def clauses_b(self):  # au plus un 'vrai' sur chaque colonne
        clauses = []
        for j in range(self.k):
            for a in range(self.n-1):
                for b in range(1+a,self.n):            
                    clauses.append([-self.code(a,j),-self.code(b,j)])
        return clauses
    
    def clauses_c(self):
        clauses = []
        for s in range(self.n):
            for a in range(self.k-1):
                for b in range(a+1, self.k):
                    clauses.append([-self.code(s, a),-self.code(s, b)])
        return clauses

    def clauses_d(self):
        clauses = []
        #print(nx.complement(self.g).edges)
        #print(self.g.edges)
        for (z,t) in self.h.edges:
            for (x, y) in nx.complement(self.g).edges:
                clauses.append([-self.code(x,z),-self.code(y,t)])
                clauses.append([-self.code(x,t),-self.code(y,z)])
        #print(len(clauses))
        return clauses

    
def reduction(G, H):
    red = Reduction(G, H)
    return red.toutes_les_clauses


def solveurISG(G, H):
    '''
    reduit G,H en probleme CLAUSE-SAT puis appelle un aolveur CLAUSE-SAT
    renvoie phi si une solution est trouvee
    [] sinon
    '''
    red = Reduction(G, H)
    sol = solve.solution(red.toutes_les_clauses)
    if sol:
        phi = []
        for ij in sol:
            if ij > -1:
                i,dump = red.decode(ij)
                phi.append(i)
        return phi
    return None



 
    
if __name__=='__main__':
    G3 = nx.Graph([(0,1),(1,2),(1,3),(2,3)])
    H3 = nx.Graph([(0,1), (0,2) ,(1,2)])

    c = Reduction(G3,H3)
   
    print("%s\n" %c.toutes_les_clauses)
    print(reduction(G3, H3))
    print(solveurISG(G3, H3))
    print(len(c.toutes_les_clauses))
 
 
