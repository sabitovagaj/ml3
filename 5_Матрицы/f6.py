import numpy as np
from scipy import linalg
A = np.array([[1,2,-4,2],[3,4,-3,1],[3,5,5,2],[-9,0,34,-5]])
print(A)
linalg.det(A)
print(linalg.det(A))