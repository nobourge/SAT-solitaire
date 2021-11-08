import projet

# contraintes

# finales
for i in range(n):
    for j in range(n):
        # non-case déja ok
        santa_clause=False
        if 0 == m1[i][j] :
            v = 1
            santa_clause=True

        elif 1 == m1[i][j] :
            # non-case déja ok
            v = 0
            santa_clause=True

        if santa_clause:
            print("ajout de %1d pour (%1d,%1d)" % (v,i,j))
            cnf.append([vpool.id((i,j,v))])
