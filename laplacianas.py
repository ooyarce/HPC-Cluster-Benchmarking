import numpy as np
from scipy.sparse import lil_matrix, eye
def matriz_laplaciana_llena(N,t=np.float32):
    e= np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)

