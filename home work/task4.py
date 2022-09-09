import numpy as np

matrix=np.zeros(25, int).reshape(5,5)
print(matrix)
print(np.diag(matrix),"\n\n")
np.fill_diagonal(matrix,np.arange(1,6))
print(matrix)
print(np.diag(matrix))