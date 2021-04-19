def ways(n,m):
        mat = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 and j==0):
                    mat[i][j] = 0
                elif(i==0):
                    mat[i][j] = 1
                elif(j==0):
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i][j-1] + mat[i-1][j]
        return mat[-1][-1]

print( ways(9,6) )