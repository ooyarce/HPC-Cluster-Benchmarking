
import petsc4py
import sys
petsc4py.init(sys.argv)
from petsc4py import PETSc
from matplotlib import pylab


def MATRIX_DENSE(n,b):
	A = PETSc.Mat().createDense([n, n]) # AIJ represents sparse matrix
	A.setUp()
	for i in range(n):
		A.setValue(i,i,2)

	#rellenar bandas
	for val in range(1,b+1):
		#rellenar hacia derecha
		j = val
		for i in range(n-j):
			A.setValue(i,j,-1)
			j+=1
		#rellenar hacia izquierda
		j = 0
		for i in range(val,n):
			A.setValue(i,j,-1)
			j+=1
	A.assemble()
	#print(A.getValues(range(n),range(n)))
	return A

def MATRIX_MPIB(n,b):
	A = PETSc.Mat().createAIJ([n, n]) # AIJ represents sparse matrix
	A.setUp()
	#rellenar diagonal
	for i in range(n):
		A.setValue(i,i,2)

	#rellenar bandas
	for val in range(1,b+1):
		#rellenar hacia derecha
		j = val
		for i in range(n-j):
			A.setValue(i,j,-1)
			j+=1
		#rellenar hacia izquierda
		j = 0
		for i in range(val,n):
			A.setValue(i,j,-1)
			j+=1

	A.assemble()
	#print(A.getValues(range(n),range(n)))
	return A

def NLIST(N,p):
	list1 = []
	for i in range(int(N/p),N+1,int(N/p)):
	    list1.append(i)
	return list1

def NAMES(NList,Ncores,Nnodes):
	names = []
	for N in NList:
		names.append(f'Sparse{N}_{Ncores}x{Nnodes}.txt')
		names.append(f'Dense{N}_{Ncores}x{Nnodes}.txt')

	return names

