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
    



