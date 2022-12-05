import petsc4py
import sys
petsc4py.init(sys.argv)
from petsc4py import PETSc
from matplotlib import pylab

def sparse(n):
	A = PETSc.Mat().createAIJ([n, n]) # AIJ represents sparse matrix
	A.setUp()
	for j in range(n-1):
		A.setValue(j,j,2)
		A.setValue(j,j+1,-1)
		A.setValue(j,j-1,-1)
	A.setValue(n-1,n-2,-1)
	A.setValue(n-1,n-1, 2)
	A.assemble()
	return A
def llena(n):
	A = PETSc.Mat().createDense([n, n]) # AIJ represents sparse matrix
	A.setUp()
	for j in range(n-1):
		A.setValue(j,j,2)
		A.setValue(j,j+1,-1)
		A.setValue(j,j-1,-1)
	A.setValue(n-1,n-2,-1)
	A.setValue(n-1,n-1, 2)
	A.assemble()
	return A
