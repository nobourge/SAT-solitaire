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
              [1, 1, 1, 1, 1], 
              [1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1, 1], 
              [-1, 1, 1, 1, -1],
              [-1, 1, 1, 1, -1]],

             [[-1, 0, 0, 0, -1], 
              [-1, 0, 0, 0, -1],
              [0, 0, 0, 0, 0], 
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0], 
              [-1, 0, 0, 0, -1],
              [-1, 0, 0, 0, -1]]]]	
	for m in l:
		m0 = []
		for i in range(len(m[0])):
			m0.append([])
			for j in range(len(m[0][i])):
				if m[i][j] == -1:
					m0[i][j] = -1
				else:
					m0[i][j] = 0
		for k in range(len(m0)):
			for n in range(len(m0[k])):
				if m0[k][n] == 0:
					m0[k][n] = 1
					if solution(m[0],m0)==True:
						print("Votre programme trouve une solution sur le couple:")
					else:
						print("Votre programme ne trouve pas de solution sur le couple:")
					print((m[0],m[1]))
					m0[k][n] = 0
					print(" \n \n")


check()
