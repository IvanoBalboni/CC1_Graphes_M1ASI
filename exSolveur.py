from pysat.formula import CNF
from pysat.solvers import Solver # , Glucose4, Glucose42, Lingeling, Minisat22, Cadical195


def toutesLesSolutions(f):
    solveur = Solver(bootstrap_with=f)
    if solveur.solve():
        print('la formule est satisfaisable\n-- toutes les solutions :')
        for m in solveur.enum_models():
            print(m)
    else:
        print("la formule n'est pas satisfaisable")

def uneSolution(f):
    solveur = Solver(bootstrap_with=f)
    if solveur.solve():
        print('la formule est satisfaisable\n-- une solution :')
        print(solveur.get_model())
    else:
        print("la formule n'est pas satisfaisable")



if __name__=='__main__':
    """
    print("\nExemple 1")
    clauses = [(1, 2), (-1, 2, -3), (1, -2, -3), (-1, -2, 3), (-1, -2, -3)]
    

    formule1 = CNF(from_clauses=clauses)
    print('\n-- la formule\n%s\n' %formule1.to_dimacs())

    toutesLesSolutions(formule1)
    uneSolution(formule1)

    print("\nExemple 2")

    formule2 = CNF(from_clauses=[(1, 2), (1, -2, -3), (-1, 2, 3), (-2, 3), (-1, -3)])
    print('\n-- la formule\n%s\n' %formule2.to_dimacs())

    toutesLesSolutions(formule2)
    """
    
    
    clauses_a = [(1,), (2, -1, -3), (2, 3, 4), (-2, -1, -3), (-1, 3, -4), (-3, 4)]
    clauses_b = [(-1, -2), (3, -4), (1, 2, 3), (1, 2, -3, 4), (1, -2, 3), (1, -3), (-1, -3, 4)]

    formule_a = CNF(from_clauses=clauses_a)
    formule_b = CNF(from_clauses=clauses_b)
    
    print('\n-- la formule a\n%s\n' %formule_a.to_dimacs())
    toutesLesSolutions(formule_a)
    uneSolution(formule_a)
    
    print('\n-- la formule b\n%s\n' %formule_b.to_dimacs())
    toutesLesSolutions(formule_b)
    uneSolution(formule_b)

    
    
    


