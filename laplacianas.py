import numpy as np
from scipy.sparse import lil_matrix, eye
def matriz_laplaciana_llena(N,t=np.float32):
    e= np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)

def list1():
    list1 = []
    for i in range(10,101,10):
        list1.append(i)

    for i in range(125,1001,25):
        list1.append(i)

    for i in range(1100,2001,100):
        list1.append(i)
    return list1