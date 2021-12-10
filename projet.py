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
from copy import deepcopy
import sys
import re
import numpy

# Données générales

CARDINALS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INTER_CARDINALS = [(1, 1), (-1, 1), (-1, -1), (1, -1)]


def afficher_solution(interpretation,
                      steps_quantity,
                      line_quantity,
                      column_quantity,
                      etats_id,
                      vpool,
                      etats):
    print("Interpretation:\n{}".format(interpretation))
    for s in range(steps_quantity + 1):
        print("Step: ", s)
        """for ind in etats_id[s]:
            if vpool.id((ind, s)) in interpretation:
                print("State {}:".format(ind))
                et = etats[ind]
                for l in et:
                    # pass
                    print('\n'.join([''.join(
                        ['{:3}'.format(tile) for tile in l])]))
                print("---" * line_quantity)"""
        for i in range(line_quantity):
            for j in range(column_quantity):
                for d in CARDINALS:
                    if vpool.id((i, j, d, s)) in interpretation:
                        pass
                        print("Coup: (", i, ",", j, ") to (",
                              i + 2 * d[0], ",", j + 2 * d[1], ")")


def in_matrix_range(line_quantity, column_quantity, y, x):
    if 0 <= y < line_quantity \
            and 0 <= x < column_quantity:
        return True


def n_etat(m2,
           line_quantity,
           column_quantity,
           potential_isolation,
           i, j, d, etat,
           balls_quantity
           ):
    """
    Fonction de transition qui tente de jouer le coup reçu sur le
    tableau reçu.

    :param potential_isolation: bool: True si le coup peut provoquer l'
    isolation d'une bille
    :param m2: list of list: état du plateau désiré
    :param line_quantity: int : quantité de ligne du plateau
    :param column_quantity: quantité de colonnes du plateau
    :param i: int: coordonnée du coup
    :param j: int: coordonnée du coup
    :param d: tuple: direction du coup
    :param etat: list of list: état depuis lequel le coup est sensé être joué
    :param balls_quantity: int: quantité de billes présentes sur le
    plateau

    :return: list of list: nouveau tableau à jour de l'état si le coup
    est légal,
            None sinon.
    """
    move = False

    if d[0] != 0:
        if etat[i + 2 * d[0]][j] == 0 and etat[i + d[0]][j] == 1 and \
                etat[i][j] == 1:
            etat[i + 2 * d[0]][j] = 1
            etat[i + d[0]][j] = 0
            etat[i][j] = 0
            #return etat
            move = True
    elif d[1] != 0:
        if etat[i][j + 2 * d[1]] == 0 and etat[i][j + d[1]] == 1 and \
                etat[i][j] == 1:
            etat[i][j + 2 * d[1]] = 1
            etat[i][j + d[1]] = 0
            etat[i][j] = 0
            #return etat
            move = True

    if move:
        if not potential_isolation:
            return etat
        else:
            if etat[i][j] == m2[i][j]:
                return etat
            else:
                #
                for d in CARDINALS:
                    for portee in range(balls_quantity):
                        if in_matrix_range(line_quantity,
                                           column_quantity,
                                           i + portee * d[0],
                                           j + portee * d[1]):

                            if etat[i + portee * d[0]][
                                j + portee * d[1]] \
                                    == 1:
                                return etat
                for d in INTER_CARDINALS:
                    for portee in range(balls_quantity - 1):
                        if in_matrix_range(line_quantity,
                                           column_quantity,
                                           i + portee * d[0],
                                           j + portee * d[1]):

                            if etat[i + portee * d[0]][
                                j + portee * d[1]] \
                                    == 1:
                                return etat


def solution(m1, m2):
    """
    prend en entrée deux matrices M et
    M' de même taille, dont les éléments sont dans {−1, 0, 1},
    construit une instance du problème SAT, et appelle un solveur
    SAT (par exemple MiniSAT22 ou Glucose3).

    :param m1: list of lists: état du plateau de départ
    :param m2: list of lists: état du plateau désiré

    :return: True s’il existe une suite de coups qui permettent de
    passer de la configuration du Solitaire qui correspond à M à
    celle qui correspond à M',
            False sinon.
    """
    # parametres
    affichage_sol = True  # affichage d'une solution
    test_unicite = False  # test si la solution est unique (si elle existe), sinon en donne une autre

    # variables ##########################
    vpool = IDPool(
        start_from=1)  # pour le stockage des identifiants entiers des couples (i,j)
    cnf = CNF()  # construction d'un objet formule en forme normale conjonctive (Conjunctive Normal Form)

    line_quantity = len(m1)
    # print("line_quantity:", line_quantity)
    column_quantity = len(m1[0])
    # print("column_quantity:", column_quantity)


    # construction de la formule

    print("Construction des clauses\n")

    # =============|
    #  contraintes |
    # =============|

    # Etat du plateau
    m1arr = numpy.array(m1)

    tiles_quantity = numpy.count_nonzero(-1 < m1arr)
    steps_quantity = 0
    for i in m1:
        steps_quantity += i.count(1)
    for i in m2:
        steps_quantity -= i.count(1)
    print("Le nombre d’étapes pour passer de m1 à m2:", steps_quantity)

    for m in (m1, m2):
        print('\n'.join([''.join(['{:3}'.format(tile) for tile in line])
                         for line in m]))
        print("---" * line_quantity)

    # Etats est un dictionnaire contenant les etats du plateau à l'étape précédente de s associés à un identificateur
    etats = {0: m1}
    #etats[0] = m1
    # etats_id est une liste contenant une liste par étape
    # Dans chaque liste elle contiendra les identificateurs des etats joués à l'étape appropriée
    etats_id = [[0]]
    for i in range(1, steps_quantity + 1):
        etats_id.append([])
    etats_id[-1].append(-1)

    #  Une clause fixant l'état du tableau au début et à la fin
    cnf.append([vpool.id((0, 0))])
    cnf.append([vpool.id((-1, steps_quantity))])

    potential_isolation = False
    for s in range(1,
                   steps_quantity + 1):  # étapes 1 à S comprises (s-1, donc commencer à 1)
        print("Etape: ", s-1)
        print("Nb etats dic: ", len(list(etats.keys())))
        # et_vals est une liste des différents états trouvés lors de l'étape en cours, ça servira plus tard
        et_vals_ids = []
        #if steps_quantity == 31:
            #print("Etape: ", s-1)
        for ind in etats_id[s - 1]:
            etat = etats[ind]  # Un état du tableau à l'étape s
            """print("Id etat: {}\nEtat:".format(ind))
            for p in etat:
                print(p)"""
            for i in range(line_quantity):
                for j in range(column_quantity):
                    for d in CARDINALS:
                        if 0 <= i + 2 * d[0] < line_quantity \
                                and 0 <= j + 2 * d[1] < column_quantity:  # Pas besoin de perdre du temps avec les coups sortant du plateau
                            balls_quantity = steps_quantity - s
                            if balls_quantity < tiles_quantity/2:
                                potential_isolation = True

                            # Déterminer l'état résultant de l'état à s et du coup
                            nouv_etat = n_etat(m2,
                                               line_quantity,
                                               column_quantity,
                                               potential_isolation,
                                               i, j, d, deepcopy(etat),
                                               balls_quantity
                                               )
                            if nouv_etat:
                                # print("Coup: ({},{}) vers ({},{})".format(i,j,i+2*d[0],j+2*d[1]))
                                if s == steps_quantity and nouv_etat == m2:  #  Si à la dernière étape l'état résultant équivaut à l'état final
                                    nouv_etat_id = -1  # On fixe son identificateur à celui de l'état final
                                else:
                                    exists = False
                                    for tmp_id in et_vals_ids:
                                        if nouv_etat == etats[tmp_id]: # Si le
                                            # nouvel état est un état qui a
                                            # déjà été crée au passé, on lui
                                            # donne l'id de l'état passé
                                            nouv_etat_id = tmp_id
                                            exists = True
                                            break
                                    if not exists:
                                        nouv_etat_id = list(etats.keys())[-1] + 1
                                        etats_id[s].append(nouv_etat_id)
                                        etats[nouv_etat_id] = nouv_etat
                                        et_vals_ids.append(nouv_etat_id)
                                """print("Id nouvel état: {}\nNouvel état:".format(nouv_etat_id))
                                for p in etats[nouv_etat_id]:
                                    print(p)
                                print()"""
                                cnf.append([-vpool.id((i, j, d, s - 1)),
                                            -vpool.id((ind, s - 1)),
                                            vpool.id(
                                                (nouv_etat_id, s))])
                            else:
                                #  Si un coup joué sur une certaine configuration du tableau ne résulte pas en un nouveau tableau légal
                                # il faut 'bannir' cette combinaison
                                cnf.append([-vpool.id((i, j, d, s - 1)),
                                            -vpool.id((ind, s - 1))])
            del etats[ind] # Garder le dictionnaire aussi petit que possible pour économiser la mémoire

    # Maximum un état par étape
    #for s in range(1, steps_quantity + 1):
        for ind in etats_id[s]:
            for ind2 in etats_id[s]:
                if ind != ind2:
                    cnf.append(
                        [-vpool.id((ind, s)), -vpool.id((ind2, s))])

    # Au moins 1 coup par étape

    #for s in range(steps_quantity):
        clauses = []
        for i in range(line_quantity):
            for j in range(column_quantity):
                for d in CARDINALS:
                    if 0 <= i + 2 * d[
                        0] < line_quantity and 0 <= j + 2 * d[
                        1] < column_quantity:
                        clauses.append(vpool.id((i, j, d, s-1)))
        cnf.append(clauses)

    print("clauses quantity:", cnf.nv)

    # phase de resolution

    solver = Glucose4(
        use_timer=True)  # pour utiliser le solveur MiniSAT
    # solver = Glucose4(use_timer=True)
    solver.append_formula(cnf.clauses, no_return=False)

    print("Resolution...")
    resultat = solver.solve()
    print("Satisfaisable : " + str(resultat))
    print("Temps de resolution : " + '{0:.2f}s'.format(solver.time()))

    if resultat:
        if affichage_sol:
            # print("\nVoici une solution: \n")
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
            afficher_solution(filtered_interpretation, steps_quantity,
                              line_quantity, column_quantity,
                              etats_id, vpool, etats)

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
                    afficher_solution(filtered_interpretation,
                                      steps_quantity, line_quantity,
                                      column_quantity, etats_id,
                                      vpool, etats)
        print("True")
        return True
