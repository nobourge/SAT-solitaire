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

def afficher_solution(interpretation):
    for i in interpretation:
        print(i)


#  todo
def n_etat(i,j,d,etat):
    if d[0] != 0:
        if etat[i+2*d[0]][j] == 0 and etat[i+d[0]][j] == 1 and etat[i][j] == 1:
            etat[i+2*d[0]][j] = 1
            etat[i+d[0]][j] = 0
            etat[i][j] = 0
            return etat
    elif d[1] != 0:
        if etat[i][j+2*d[1]] == 0 and etat[i][j+d[1]] == 1 and etat[i][j] == 1:
            etat[i][j+2*d[1]] = 1
            etat[i][j+d[1]] = 0
            etat[i][j] = 0
            return etat

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

    # Données générales
    #D = {(1, 0): 1, (0, 1): 2, (-1, 0): 3, (0, -1): 4}
    D = [(1,0),(0,1),(-1,0),(0,-1)]

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
        print('\n'.join([''.join(['{:3}'.format(tile) for tile in line])
                         for line in m]))
        print("---"*line_quantity)
    # les valeurs du tableau de d́epart A1 et du tableau de fin AS
    # sont fix́ees
    etats = {-1:m2}
    etats[0] = m1
    etats_id = [[0]]
    for i in range(1,steps_quantity+1):
        etats_id.append([])
    etats_id[-1].append(-1)

    cnf.append([vpool.id((0,0))])
    cnf.append([vpool.id((-1,steps_quantity))])
    # Première, apparition d'une bille
    et_vals = list(etats.values())
    for s in range(1, steps_quantity+1): # étapes 1 à S comprises (s-1, donc commencer à 1)
        #print("Etape: ", s-1)
        for ind in etats_id[s-1]:                       
            etat = etats[ind]
            #print("Id etat: {}\nEtat:".format(ind))
            for p in etat:
                pass
                #print(p)
            for i in range(line_quantity):
                for j in range(column_quantity):
                    for d in D:
                        if 0<=i+2*d[0]<line_quantity and 0<=j+2*d[1]<column_quantity: 
                            n_et = n_etat(i,j,d,deepcopy(etat))
                            if n_et :
                                #print("Coup: ({},{}) vers ({},{})".format(i,j,i+2*d[0],j+2*d[1]))  
                                if s == steps_quantity and n_et == m2:
                                    n_e_id = -1
                                elif n_et in et_vals: # unique states
                                    n_e_id = et_vals.index(n_et) - 1 # Skewed because of state id -1 
                                else:
                                    n_e_id = list(etats.keys())[-1]+1
                                    etats_id[s].append(n_e_id)
                                    etats[n_e_id] = n_et
                                    et_vals = list(etats.values())
                                #print("Id nouvel état: {}\nNouvel état:".format(n_e_id))
                                for p in etats[n_e_id]:
                                    pass
                                    #print(p)
                                #print()
                                cnf.append([-vpool.id((i,j,d,s-1)),-vpool.id((ind,s-1)),vpool.id((n_e_id,s))])
                            else:
                                cnf.append([-vpool.id((i,j,d,s-1)),-vpool.id((ind,s-1))])

    # Maximum un état par étape
    for s in range(1, steps_quantity+1):
        for ind in etats_id[s]:
            for ind2 in etats_id[s]:
                if ind != ind2:
                    cnf.append([-vpool.id((ind, s)), -vpool.id((ind2, s))])

    # Au moins 1 coup par étape

    for s in range(steps_quantity):
        clauses = []
        #for ind in etats_id[s]:
        for i in range(line_quantity):
            for j in range(column_quantity):
                for d in D:
                    if 0<=i+2*d[0]<line_quantity and 0<=j+2*d[1]<column_quantity: 
                        clauses.append(vpool.id((i, j, d, s)))
        cnf.append(clauses)
    

    print("clauses quantity:", cnf.nv)
    # print("clauses:", cnf.clauses)

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
            #print("\nVoici une solution: \n")
            interpretation = solver.get_model()  # extracting a
            # satisfying assignment for CNF formula given to the solver
            # A model is provided if a previous SAT call returned True.
            # Otherwise, None is reported.
            # Return type list(int) or None

            # cette interpretation est longue,
            # on va filtrer les valeurs positives
            # (il y a en line_quantity fois moins)
            filtered_interpretation = list(filter(lambda x: x >= 0, interpretation))
            #afficher_solution(filtered_interpretation)
            print("filtered_interpretation:\n{}".format(filtered_interpretation))
            for ind in filtered_interpretation:
                #pass
                print(vpool.obj(ind))
            print()
            for s in range(steps_quantity+1):
                print("Step: ",s)
                for ind in etats_id[s]:
                    if vpool.id((ind, s)) in filtered_interpretation:
                        print("State {}:".format(ind))
                        et = etats[ind]
                        for l in et:
                            #pass
                            print(l)
                for i in range(line_quantity):
                    for j in range(column_quantity):
                        for d in D:
                            if vpool.id((i, j, d, s)) in filtered_interpretation:
                                #pass
                                print("Coup: (", i, ",", j,") to (", i + 2 * d[0], ",",j + 2 *d[1], ")")
                                        
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
                    #afficher_solution(filtered_interpretation)
                    for s in range(steps_quantity):
                        MS = []
                        for i in range(line_quantity):
                            MS.append([])
                            for j in range(column_quantity):
                                for d in D:
                                    if vpool.id((i, j, d,s)) in filtered_interpretation:
                                        print("step", s, ": (", i, ",",j,") to (", i + 2 * d[0],",",j + 2 *d[1], ")")
        print("True")
        return True
    elif cnf.nv == 152 or cnf.nv == 1837 or cnf.nv == 880:
        interpretation = solver.get_core()
        print("interpretation:")
        print(interpretation)
        for cl in cnf.clauses:
            if vpool.id((-1,steps_quantity)) in cl or vpool.id((4,6,(0,-1),3)) in cl or -vpool.id((4,6,(0,-1),3)) in cl:
                if len(cl) !=2 and len(cl) < 5:
                    print("Clause:", cl)
                    print("Objects:")
                    for i in cl:
                        if i < 0:
                            print(vpool.obj(-i))    
                        else:
                            print(vpool.obj(i))
