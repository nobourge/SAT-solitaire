#!/usr/bin/env python3.6
# cours informatique fondamentale 2021-2022
# chapitre SAT
# probleme du Solitaire
"""
il faut passer en arguments deux matrices
(codées sous forme de listes de listes)
M et M' de même taille,
dont les éléments sont dans {−1, 0, 1}
exemple 'python3 solution.py matrix/3/1 matrix/3/2'
va prendre la matrice 1 de dimension 3x3
et renvoyer
true s’il existe une suite de coups
qui permettent de passer de la configuration
du Solitaire qui correspond à M à celle qui correspond à M',
False sinon
"""
from pysat.solvers import Minisat22
from pysat.solvers import Glucose4
from pysat.formula import CNF
from pysat.formula import IDPool
import sys
import re


def afficher_solution(interpretation):
    for i in interpretation:
        print(i)
#  todo


def solution(m1, m2):
    # parametres
    affichage_sol = True  # affichage d'une solution
    test_unicite = False  # test si la solution est unique (si elle existe), sinon en donne une autre

    # variables ##########################
    vpool = IDPool(
        start_from=1)  # pour le stockage des identifiants entiers des couples (i,j)
    cnf = CNF()  # construction d'un objet formule en forme normale conjonctive (Conjunctive Normal Form)
    line_quantity = len(m1)
    print("line_quantity:", line_quantity)
    column_quantity = len(m1[0])
    print("column_quantity:", column_quantity)

    trous = []

    # construction de la formule

    print("Construction des clauses\n")

    # contraintes

    # finales
    for i in range(line_quantity):
        for j in range(column_quantity):
            v = m1[i][j]
            if 0 < v:
                # non-case déja ok
                print("ajout de %1d pour (%1d,%1d)" % (v, i, j))
                cnf.append([vpool.id((i, j, m2[i][j]))])

    # trois cases adjacentes

    # sur une même ligne ou colonne

    # deux billes

    # une sur la case du milieu

    # bille qui se trouve sur une des extr´emit´es saute par dessus la bille du milieu, pour la faire atterrir dans le trou qui se trouve `a
    # l’autre extr´emit´e.

    # bille du milieu du plateau supprimée
    """
    # au plus une valeur par case (contrainte pas necessaire car elle est une consequence des autres)
    # permet d'accelerer la resolution

    print("Au plus une valeur par case")

    for i in range(line_quantity):
        for j in range(column_quantity):
            for v1 in range(2):
                for v2 in range(v1 + 1, 2):
                    cnf.append([-vpool.id((i, j, v1 + 1)),
                                -vpool.id((i, j, v2 + 1))])
    """
    print("clauses quantity:", cnf.nv)
    print("clauses:", cnf.clauses)

    # phase de resolution

    solver = Minisat22(
        use_timer=True)  # pour utiliser le solveur MiniSAT
    # solver = Glucose4(use_timer=True)
    solver.append_formula(cnf.clauses, no_return=False)

    print("Resolution...")
    resultat = solver.solve()
    print("Satisfaisable : " + str(resultat))
    print("Temps de resolution : " + '{0:.2f}s'.format(solver.time()))

    if resultat:
        if affichage_sol:
            print("\nVoici une solution: \n")
            interpretation = solver.get_model() # extracting a
            # satisfying assignment for CNF formula given to the solver
            # A model is provided if a previous SAT call returned True.
            # Otherwise, None is reported.
            # Return type list(int) or None

            # cette interpretation est longue,
            # on va filtrer les valeurs positives
            # (il y a en line_quantity fois moins)
            filtered_interpretation = list(
                filter(lambda x: x >= 0, interpretation))
            afficher_solution(filtered_interpretation)

            # test d'unicite
            if test_unicite:
                d = []
                for i in range(line_quantity):
                    for j in range(line_quantity):
                        for v in range(line_quantity):
                            if vpool.id((i, j,
                                         v + 1)) in filtered_interpretation:
                                d.append(-vpool.id((i, j, v + 1)))
                solver.add_clause(d)
                not_unique = solver.solve()  # solution pas unique si la formule est satisfaisable
                if not not_unique:
                    print("Solution unique")
                else:
                    print(
                        "\nSolution pas unique, en voici une autre:\n")
                    interpretation = solver.get_model()
                    filtered_interpretation = list(
                        filter(lambda x: x >= 0, interpretation))
                    afficher_solution(filtered_interpretation)
        print("True")
        return True