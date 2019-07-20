import numpy as np
import cs

def readm(fname ='A.csv'):
        f = open(fname, 'r') # w,b
        A = []
        for line in f.readline():
            A.append( [float(x) for x in line.strip().split(',')] )
        print(A)
        f.close()
    return A


def printm(m):
    for row in m :
        print( ''.join( [ f' {x:5.2}' for x in row ]) )