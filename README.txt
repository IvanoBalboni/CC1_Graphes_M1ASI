Pour generer les tests, executer la commande python3 exGraphe.py

Il semblerait que la fonction exemplesInstancesPositives(n)
peut entrer dans une boucle infinie avec le flag qui reste a True.
Cela se produit aproximativement 1 fois tous les 30 appels avec n >= 9.
Soit en moyenne autour de 10 executions de exGraphe.py (3 appels).
le nombre maximum d'executions sans erreurs enregistres est de 19.
Cela semble se produire lorsque le nombre d'arretes est insuffisant.
