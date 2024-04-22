import numpy as np
from scipy import linalg
A=np.array([[1,2,-4],[3,4,9],[-3,8,-3]])
print("Матрица имеет вид",A)
linalg.norm(A)
print("Норма1 равно",linalg.norm(A)) #5.4772255750516612
linalg.norm(A,'fro') # frobenius norm is the default
print("Норма2 равно",linalg.norm(A,'fro')) #5.4772255750516612
linalg.norm(A,1) # L1 norm (max column sum)
print("Норма3 равно",linalg.norm(A,1))#6
linalg.norm(A,-1)
print("Норма4 равно",linalg.norm(A,-1))#4
linalg.norm(A,np.inf) # L inf norm (max row sum)
print("Норма5 равно",linalg.norm(A,np.inf))#7"Норма1 равно",