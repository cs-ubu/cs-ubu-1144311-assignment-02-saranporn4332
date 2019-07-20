
from mat import *

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b)n
    import num as np
    A,b = np.array(A), np.array(b)
    n = len(A[0])
    x = [0]*n
    #1. Elimination
    n = len(A[0])
    print(f' n = {n}')
    for k in range(n-1)
        print(f'เลือกสมการที่ {k}')
        for j in range(k+1, n):
            print(f'\t กำจัดตัวแปรที่ {k},ออกจากสมการที่ {j}')
            lam = A[j] [k] / A [k] [k]
            # update A [j][k.....เป็นต้นไป......]
        #    A[j][k+1] = A[j][k+1] - lam * A[k]
        #    A[j][k+2] = A[j][k+2] - lam * A[k]
        #    A[j][k+3] = A[j][k+3] - lam * A[k]
            A[j, k + 1 : n] = A[j, k + 1 : n ] - lam * A[k, k + 1 : n]

        #    print(f'\t\tlambda= {lam}')  
        # update b [j] 
            b[j] = b[j] - lam * b[j]                                    
        print(A)

    #2. Back Substitution
    x[n-1] = b[n-1] / A[n-1][n-1]
    for k in range(n-1, -1 , -1):
        print(f'back sub k={k}')
    #    A[k,0:n]*x[k:] = b[k:]
        x[k] = (b[k] - np.dot(A[k,k+1:n], x[k+1:n]))/A[k,k]
    return x.flatten()




'''print('====A====')
print(A)
print('====b====')
print(b)
print( solve(A,b))
'''
