from copy import deepcopy
from sympy import LeviCivita
from colorama import Fore, Style
from projet import solution

R_matrices_list = []

for size in range(5, 7):
    print(Fore.BLUE + "size:", size, "--------------------------------")
    print(Style.RESET_ALL)

    matrix1 = []

    matrix2 = []

    mr = []

    for i in range(size):
        matrix1.append([])

        matrix2.append([])

        mr.append([])
        for j in range(size):

            if (i in [0, size - 1] and j in [0, size - 1, 1, size - 2]) \
                    or (i in [1, size - 2] and j in [0, size - 1]):
                matrix1[i].append(-1)
                matrix2[i].append(-1)
                mr[i].append(-1)
            else:
                matrix1[i].append(1)
                matrix2[i].append(0)
                mr[i].append(0)

    for i in range(size):
        for j in range(size):

            if matrix1[i][j] == -1:
                pass

            else:
                print("(", i, ",", j, ")")

                matrixa = deepcopy(matrix1)
                matrixa[i][j] = 0
                print("ma")

                for line in matrixa:
                    print('\n'.join([''.join(
                        ['{:3}'.format(tile) for tile in line])]))
                print("---------------------------")

                """
    
                matrix2 = LeviCivita(matrix1)
                print(matrix2)
                """
                matrixs = deepcopy(matrix2)
                matrixs[i][j] = 1
                print("ms")

                for line in matrixs:
                    print('\n'.join([''.join(
                        ['{:3}'.format(tile) for tile in line])]))
                print("---------------------------")

                if solution(matrixa, matrixs) == True:
                    mr[i][j] = 1
                else:
                    mr[i][j] = 3

                print(Fore.RED + "mr", "(", i, ",", j, ")")
                print(Style.RESET_ALL)

                for line in mr:
                    print('\n'.join([''.join(
                        ['{:3}'.format(tile) for tile in line])]))
                print("---------------------------")
    R_matrices_list.append(mr)

for m in R_matrices_list:
    for line in m:
        print('\n'.join([''.join(
            ['{:3}'.format(tile) for tile in line])]))
    print("---------------------------")
