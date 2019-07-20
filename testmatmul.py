from matmul import readm, matmul

#1. read matrix A from 'A.csv'   
A = readm('A.csv')

#2. read matrix A from 'A.csv
A = readm('b.csv')

#3. find the result of C = A x b
def matmul(A,b):
    m, n = len(A), len(b[0])
    J = len( A[0] ) # A-mxJ #b -Jxn
    if len(A[0]) == len(b):
        #C = [ [0]*n for i in range(n) ]
        C = [[0]*n]*m
       # A[0][0]*b[0][0] + A[0][1]*b[1][0] + A[0][2]*b[2][0]
        for r in range(m):
            for c in range(n): 
                C[r][c] = sum([float(A[c][j])*float(b[j][c]) for j in range(J)])
        return C
    return [] #  ไม่สามารถดูได้
#4. print C
print(matmul(A,b))
C = matmul(A,b)
for row in C :
    print(row)
print(".....")





import numpy as np
import csv


#อ่านไฟล์ & เขียนไฟล์
A = readm('A.csv')
f = open('A.csv','r')# w,b
A = []
for line in f.readline():
    A.append( [float(x) for x in line.strip().split(',')] )
print(A)
f.close()


def csv2mat(filename):
    return np.array(list(csv.reader(open(filename,"rt"),delimiter=",")))
A = csv2mat('A.csv')
b = csv2mat('b.csv')
print(A)
print(b)

#3. find the result of C = A x b
def matmul(A,b):
    m, n = len(A), len(b[0])
    J = len( A[0] ) # A-mxJ #b -Jxn
    if len(A[0]) == len(b):
        #C = [ [0]*n for i in range(n) ]
        C = [[0]*n]*m
       # A[0][0]*b[0][0] + A[0][1]*b[1][0] + A[0][2]*b[2][0]
        for r in range(m):
            for c in range(n): 
                C[r][c] = sum([float(A[c][j])*float(b[j][c]) for j in range(J)])
        return C
    return [] #  ไม่สามารถดูได้
#4. print C
print(matmul(A,b))
C = matmul(A,b)
for row in C :
    print(row)
print(".....")
D = np.dot(np.array(A) )
