from copy import deepcopy
from sympy import LeviCivita

from projet import solution

size = 7
matrix1 = [[-1, -1, 1, 1, 1, -1, -1],
           [-1, 1, 1, 1, 1, 1, -1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [-1, 1, 1, 1, 1, 1, -1],
           [-1, -1, 1, 1, 1, -1, -1]]

matrix2 = [[-1, -1, 0, 0, 0, -1, -1],
           [-1, 0, 0, 0, 0, 0, -1],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [-1, 0, 0, 0, 0, 0, -1],
           [-1, -1, 0, 0, 0, -1, -1]]

mr = [[-1, -1, 0, 0, 0, -1, -1],
      [-1, 0, 0, 0, 0, 0, -1],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [-1, 0, 0, 0, 0, 0, -1],
      [-1, -1, 0, 0, 0, -1, -1]]

for i in range(size):
    for j in range(size):
        if matrix1[i][j] == -1:
            pass

        else:
            matrixa = deepcopy(matrix1)
            matrixa[i][j] = 0
            print("ma")

            print("(", i, ",", j, ")")

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

            print("(", i, ",", j, ")")

            for l in matrixs:
                print('\n'.join([''.join(
                    ['{:3}'.format(tile) for tile in l])]))
            print("---------------------------")
            if solution(matrixa, matrixs) == True:
                mr[i][j] = 1

            print("mr", "(", i, ",", j, ")")

            for l in mr:
                print('\n'.join([''.join(
                    ['{:3}'.format(tile) for tile in l])]))
            print("---------------------------")
