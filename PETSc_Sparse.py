import petsc4py
import sys
petsc4py.init(sys.argv)
from petsc4py import PETSc
from matplotlib import pylab

def MATRIX_MPI(n):
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
def MATRIX_MPIB(n,b):
	A = PETSc.Mat().createAIJ([n, n]) # AIJ represents sparse matrix
	A.setUp()
	#rellenar diagonal
	for i in range(n):
		A.setValue(i,i,2)
	#rellenar bandas
	for val in range(1,b+1):
		j = val
		#rellenar hacia derecha
		for i in range(n-j):
			A.setValue(i,j,-1)
			j+=1
	#rellenar hacia izquierda
	for val in range(1,b+1):
		j = 0
		for i in range(val,n):
			A.setValue(i,j,-1)
			j+=1
	A.assemble()
	return A
def list1():
	list1 = []
	for i in range(10,101,10):
	    list1.append(i)

	for i in range(125,1001,25):
	    list1.append(i)

	for i in range(1100,2001,100):
	    list1.append(i)
	return list1



