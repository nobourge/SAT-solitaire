from projet import solution

def check():
	l=[[[[1,0,0],[1,0,0],[0,1,0]],[[0,0,0],[0,0,0],[0,0,1]]],[[[-1,1,-1],[-1,1,-1],[-1,0,-1]],[[-1,0,-1],[-1,0,-1],[-1,1,-1]]],[[[0,1,0,-1],[1,1,1,1],[0,-1,1,1]],[[0,0,0,-1],[0,1,0,1],[1,-1,0,1]]],[[[-1,-1,-1,1,-1,-1,-1],[-1,-1,0,1,0,-1,-1],[-1,0,0,0,1,0,-1],[1,1,0,0,0,1,0],[0,0,1,0,1,0,0],[-1,1,0,0,0,0,-1],[-1,-1,0,0,0,0,-1],[-1,-1,-1,0,-1,-1,-1]],[[-1,-1,-1,0,-1,-1,-1],[-1,-1,0,0,0,-1,-1],[-1,0,0,0,0,0,-1],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1]]],[[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[1,1,0,1,0,0,0],[0,0,1,0,0,1,1],[-1,1,1,0,0,0,-1],[-1,-1,0,0,0,-1,-1]],[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[-1,0,1,1,0,0,-1],[-1,-1,0,0,0,-1,-1]]]]
	s=[[[[1,0],[1,0]],[[0,1],[0,0]]],[[[1,1,0],[1,1,0],[0,0,1]],[[0,0,0],[0,1,0],[1,0,1]]],[[[1,0,-1,1],[1,-1,0,1],[1,1,0,0],[1,0,-1,1]],[[1,0,-1,0],[1,-1,0,1],[0,0,0,0],[0,0,-1,0]]],[[[-1,1,1,-1],[1,0,1,1],[1,1,1,1],[-1,1,1,-1]],[[-1,0,0,-1],[0,1,0,0],[0,0,0,0],[-1,0,0,-1]]]]
	for m in l:
		if solution(m[0],m[1])!=True:
			print("Votre programme échoue sur le couple:")
		else:
			print("Votre programme marche sur le couple:")
		print((m[0],m[1]))
	for m in s:
		if solution(m[0],m[1])==True:
			print("Votre programme échoue sur le couple:")
		else:
			print("Votre programme marche sur le couple:")
		print((m[0],m[1]))
	m1=[[[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1]],[[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]]
	if solution(m1[0],m1[1])!=True:
		print("Votre programme échoue sur le couple:")
	else:
		print("Votre programme marche sur le couple:")
	print((m1[0],m1[1]))
	m2=[[[-1,1,1,1,-1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[-1,1,1,1,-1]],[[-1,0,0,0,-1],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[-1,0,0,0,-1]]]
	if solution(m2[0],m2[1])==True:
		print("Votre programme échoue sur le couple:")
	else:
		print("Votre programme marche sur le couple:")
	print((m2[0],m2[1]))

check()
