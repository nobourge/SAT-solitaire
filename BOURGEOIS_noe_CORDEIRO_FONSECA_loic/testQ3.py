from projet import solution


def check():
    l = [[[[-1, -1, 1, -1, -1],
           [-1, 1, 1, 1, -1],
           [1, 1, -1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 0, 1, 1],
           [-1, 1, 1, 1, -1],
           [-1, -1, 1, -1, -1]],

          [[-1, -1, 0, -1, -1],
           [-1, 0, 0, 0, -1],
           [0, 0, -1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [-1, 0, 0, 0, -1],
           [-1, -1, 0, -1, -1]]],

         [[[-1, 1, 1, 1, -1],
           [1, 1, 1, 1, 1],
           [1, 1, 0, 1, 1],
           [1, 1, 1, 1, 1],
           [-1, 1, 1, 1, -1]],

          [[-1, 0, 0, 0, -1],
           [0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [-1, 0, 0, 0, -1]]],
         [
             [[-1, 1, 1, -1, -1],
              [-1, 1, 1, -1, -1], 
              [1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1], 
              [1, 1, 1, 1, 1],
              [-1, 1, 1, -1, -1]],

             [[-1, 0, 0, -1, -1],
              [-1, 0, 0, -1, -1], 
              [0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0], 
              [0, 0, 0, 0, 0],
              [-1, 0, 0, -1, -1]]], 
            [
             [[-1, 1, 1, 1, -1], 
             [-1, 1, 1, 1, -1],
              [1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1], 
              [-1, 1, 1, 1, -1],
              [-1, 1, 1, 1, -1]],

             [[-1, 0, 0, 0, -1], 
              [-1, 0, 0, 0, -1],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0], 
              [-1, 0, 0, 0, -1],
              [-1, 0, 0, 0, -1]]]]
    for m in l:
        if solution(m[0], m[1]) != True:
            print("Votre programme échoue sur le couple:")
        else:
            print("Votre programme marche sur le couple:")
        print((m[0], m[1]))
        print(" \n \n")
    print(" \n \n")


check()
