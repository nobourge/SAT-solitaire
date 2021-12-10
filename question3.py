from projet import solution


def check():
    l = [[[[-1, -1, 1, 1, 1, -1, -1],
           [-1, 1, 1, 1, 1, 1, -1],
           [1, 1, 1, -1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 0, 1, 1, 1],
           [-1, 1, 1, 1, 1, 1, -1],
           [-1, -1, 1, 1, 1, -1, -1]],

          [[-1, -1, 0, 0, 0, -1, -1],
           [-1, 0, 0, 0, 0, 0, -1],
           [0, 0, 0, -1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [-1, 0, 0, 0, 0, 0, -1],
           [-1, -1, 0, 0, 0, -1, -1]]],

         [[[-1, -1, -1, 1, 1, 1, -1, -1, -1],
           [-1, -1, -1, 1, 1, 1, -1, -1, -1],
           [-1, -1, -1, 1, 1, 1, -1, -1, -1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1],
           [-1, -1, -1, 1, 1, 1, -1, -1, -1],
           [-1, -1, -1, 1, 1, 1, -1, -1, -1],
           [-1, -1, -1, 1, 1, 1, -1, -1, -1]],

          [[-1, -1, -1, 0, 0, 0, -1, -1, -1],
           [-1, -1, -1, 0, 0, 0, -1, -1, -1],
           [-1, -1, -1, 0, 0, 0, -1, -1, -1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [-1, -1, -1, 0, 0, 0, -1, -1, -1],
           [-1, -1, -1, 0, 0, 0, -1, -1, -1],
           [-1, -1, -1, 0, 0, 0, -1, -1, -1]]],

         [[[-1, -1, 1, 1, 1, -1, -1, -1],
           [-1, -1, 1, 1, 1, -1, -1, -1],
           [-1, -1, 1, 1, 1, -1, -1, -1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [-1, -1, 1, 1, 1, -1, -1, -1],
           [-1, -1, 1, 1, 1, -1, -1, -1]],

          [[-1, -1, 0, 0, 0, -1, -1, -1],
           [-1, -1, 0, 0, 0, -1, -1, -1],
           [-1, -1, 0, 0, 0, -1, -1, -1],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [-1, -1, 0, 0, 0, -1, -1, -1],
           [-1, -1, 0, 0, 0, -1, -1, -1]]],

         [[[-1, -1, -1, 1, -1, -1, -1],
           [-1, -1, 1, 1, 1, -1, -1],
           [-1, 1, 1, 1, 1, 1, -1],
           [1, 1, 1, 0, 1, 1, 1],
           [-1, 1, 1, 1, 1, 1, -1],
           [-1, -1, 1, 1, 1, -1, -1],
           [-1, -1, -1, 1, -1, -1, -1]],

          [[-1, -1, -1, 0, -1, -1, -1],
           [-1, -1, 0, 0, 0, -1, -1],
           [-1, 0, 0, 0, 0, 0, -1],
           [0, 0, 0, 1, 0, 0, 0],
           [-1, 0, 0, 0, 0, 0, -1],
           [-1, -1, 0, 0, 0, -1, -1],
           [-1, -1, -1, 0, -1, -1, -1]]]]

    for m in l:


        for line in m[0]:
            print('\n'.join([''.join(
                ['{:3}'.format(tile) for tile in line])]))
        print("---------------------------")

        for line in m[1]:
            print('\n'.join([''.join(
                ['{:3}'.format(tile) for tile in line])]))
        print("---------------------------")

        if solution(m[0], m[1]) == True:
            print(
                "Votre programme trouve une solution sur le couple:")
        else:
            print(
                "Votre programme ne trouve pas de solution sur le couple:")
        print(" \n \n")


check()