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
# from pysat.solvers import Glucose4
from pysat.formula import CNF
from pysat.formula import IDPool
# import sys
# import re

# Données générales
D = {(1, 0): 6, (0, 1): 3, (-1, 0): 12, (0, -1): 9}


def afficher_solution(interpretation,
                      steps_quantity,
                      line_quantity,
                      column_quantity,
                      vpool):
    for s in range(steps_quantity):
        for i in range(line_quantity):
            for j in range(column_quantity):
                for d in D:
                    if vpool.id((i, j, D[d], s)) in interpretation:
                        print("step", s, ": (",
                              i, ",", j,
                              ")", D[d], " to (", i + 2 * d[0], ",",
                              j + 2 * d[1], ")")


def solution(m1, m2):
    print("--------------------------------------------")
    # variables ##########################
    # stockage des identifiants entiers des clauses
    vpool = IDPool(start_from=1)
    # construction d'un objet formule en forme normale conjonctive
    # (Conjunctive Normal Form)
    cnf = CNF()

    # parametres
    affichage_sol = True  # affichage d'une solution
    # test si la solution est unique (si elle existe),
    # sinon en donne une autre:
    # test_unicite = False
    test_unicite = True

    line_quantity = len(m1)
    print("line_quantity:", line_quantity)
    column_quantity = len(m1[0])
    print("column_quantity:", column_quantity)

    # construction de la formule

    print("Construction des clauses\n")

    # =============|
    # contraintes |
    # =============|

    # Etat du plateau

    steps_quantity = 0
    for i in m1:
        steps_quantity += i.count(1)
    for i in m2:
        steps_quantity -= i.count(1)
    print("le nombre d’ étapes pour passer de m1 à m2:",
          steps_quantity)

    for m in (m1, m2):
        print('\n'.join([''.join(['{:3}'.format(tile if -1 < tile
                                                else " ") for tile in
                                  line])
                         for line in m]))
        print("---" * line_quantity)

    # les valeurs du tableau de d́epart A1 et du tableau de fin AS
    # sont fix́ees

    for i in range(line_quantity):
        for j in range(column_quantity):

            vm1 = m1[i][j]
            if -1 < m1[i][j]:
                vm2 = m2[i][j]
                # print("%1d pour la case (%1d,%1d) à l'étape %1d"
                #    % (vm1, i, j, 0))
                cnf.append([vpool.id((i,
                                      j,
                                      vm1,
                                      0))])
                # print("%1d pour la case (%1d,%1d) à l'étape %1d"
                #    % (vm2, i, j, steps_quantity))
                cnf.append([vpool.id((i,
                                      j,
                                      vm2,
                                      steps_quantity))])

    # Maximum une valeur par case

    # print("Maximum une valeur par case")
    for i in range(line_quantity):
        for j in range(column_quantity):
            if -1 < m1[i][j]:
                for s in range(0, steps_quantity + 1):
                    for v1 in range(0, 2):
                        cnf.append([-vpool.id((i, j, 0, s)),
                                    -vpool.id((i, j, 1, s))])

    # Clauses temporelles

    for i in range(line_quantity):
        for j in range(column_quantity):
            if -1 < m1[i][j]:
                for s in range(1, steps_quantity + 1):
                    for d in D:
                        if i - d[0] < line_quantity and \
                                j - d[1] < column_quantity and \
                                (i - 2 * d[0]) < line_quantity and \
                                (j - 2 * d[1]) < column_quantity:

                            if -1 < m1[i - d[0]][j - d[1]] and \
                                    -1 < m1[i - 2 * d[0]][j - 2 * d[1]]:

                                cnf.append([-vpool.id((i - 2 * d[0],
                                                       j - 2 * d[1],
                                                       1, s - 1)),
                                            -vpool.id((i - d[0],
                                                       j - d[1],
                                                       1, s - 1)),

                                            -vpool.id((i, j, 0, s - 1)),

                                            -vpool.id((i - 2 * d[0],
                                                       j - 2 * d[1],
                                                       D[d],
                                                       s - 1)),

                                            -vpool.id((i - 2 * d[0],
                                                       j - 2 * d[1],
                                                       0, s)),
                                            -vpool.id((i - d[0],
                                                       j - d[1],
                                                       0, s)),

                                            vpool.id((i, j, 1, s))])
                                """
                                cnf.append([vpool.id((i, j, 1, s - 1)),
                                            -vpool.id((i, j, 0, s))])
                                cnf.append([-vpool.id((i - d[0],
                                                       j - d[1],
                                                       D[d],
                                                       s - 1)),
                                            vpool.id((i, j, 0, s))])
                                cnf.append([vpool.id((i - d[0],
                                                      j - d[1],
                                                      D[d],
                                                      s - 1)),
                                            -vpool.id(
                                                (i, j, 1, s - 1))])
                                """
                                """
                                cnf.append([vpool.id((i, j, 0, s - 1)),
                                            -vpool.id((i, j, 1, s))])
                                cnf.append([-vpool.id((i - 2 * d[0],
                                                       j - 2 * d[1],
                                                       D[d],
                                                       s - 1)),
                                            vpool.id((i, j, 1, s))])
                                cnf.append([vpool.id((i - 2 * d[0],
                                                      j - 2 * d[1],
                                                      D[d],
                                                      s - 1)),
                                            -vpool.id(
                                                (i, j, 0, s - 1))])
                                """

    # Max un coup par étape

    for s in range(1, steps_quantity + 1):

        for i in range(line_quantity):
            for j in range(column_quantity):
                if -1 < m1[i][j]:
                    for d in D:

                        for ip in range(line_quantity):
                            for jp in range(column_quantity):
                                if -1 < m1[ip][jp]:
                                    for dp in D:

                                        if ip != i or \
                                                jp != j or \
                                                dp != d:
                                            cnf.append([
                                                -vpool.id(
                                                    (i, j, D[d], s)),
                                                -vpool.id((
                                                          ip, jp, D[dp],
                                                          s))])
    # Au moins 1 coup par étape

    for s in range(steps_quantity + 1):
        clauses = []
        for i in range(line_quantity):
            for j in range(column_quantity):
                for d in D:
                    clauses.append(vpool.id((i, j, D[d], s)))
        cnf.append(clauses)

    # pas le meme coup 2 etapes consecutives
    for s in range(steps_quantity):
        for i in range(line_quantity):
            for j in range(column_quantity):
                for d in D:
                    cnf.append([-vpool.id((i, j, D[d], s)),
                               -vpool.id((i, j, D[d], s + 1))])


    print("clauses quantity:", cnf.nv)
    # print("clauses:", cnf.clauses)

    # phase de resolution

    solver = Minisat22(
        use_timer=True)  # pour utiliser le solveur MiniSAT
    # solver = Glucose4(use_timer=True)
    solver.append_formula(cnf.clauses, no_return=False)

    # print("Resolution...")
    resultat = solver.solve()
    print("Satisfaisable : " + str(resultat))
    print("Temps de resolution : " + '{0:.2f}s'.format(solver.time()))

    if resultat:
        if affichage_sol:
            print("\nVoici une solution: \n")
            interpretation = solver.get_model()  # extracting a
            # satisfying assignment for CNF formula given to the solver
            # A model is provided if a previous SAT call returned True.
            # Otherwise, None is reported.
            # Return type list(int) or None

            # cette interpretation est longue,
            # on va filtrer les valeurs positives
            # (il y a en line_quantity fois moins)
            filtered_interpretation = list(
                filter(lambda x: x >= 0, interpretation))
            afficher_solution(# filtered_interpretation,
                              interpretation,
                              steps_quantity,
                              line_quantity,
                              column_quantity,
                              vpool)
            """
            # test d'unicite
            if test_unicite:
                other = []
                for s in range(steps_quantity):
                    for i in range(line_quantity):
                        for j in range(line_quantity):
                            for d in D:
                                if vpool.id((i, j,
                                             D[d] + 1)) in \
                                        filtered_interpretation:
                                    other.append(-vpool.id((i, j, d,
                                                            s)))
                solver.add_clause(other)
                not_unique = solver.solve()
                # solution pas unique si la formule est satisfaisable
                if not not_unique:
                    print("Solution unique")
                else:
                    print(
                        "\nSolution pas unique, en voici une autre:\n")
                    interpretation = solver.get_model()
                    filtered_interpretation = list(
                        filter(lambda x: x >= 0, interpretation))
                    # afficher_solution(filtered_interpretation,
                    afficher_solution(interpretation,
                                      steps_quantity,
                                      line_quantity,
                                      column_quantity,
                                      vpool)
"""
        print("True")
        return True
