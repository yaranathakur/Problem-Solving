def transpose(matrix, n):
    
    m_transpose = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            m_transpose[j][i] = matrix[i][j]
            
    for row in m_transpose:
        print(row)

m = [[1, 1, 1, 1], 
     [2, 2, 2, 2], 
     [3, 3, 3, 3], 
     [4, 4, 4, 4]]
n = 4
transpose(m, n)