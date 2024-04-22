import numpy as np
from scipy import linalg
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
print(A)
linalg.inv(A)
A.dot(linalg.inv(A)) #double check
print(linalg.inv(A))
print(A.dot(linalg.inv(A)))

