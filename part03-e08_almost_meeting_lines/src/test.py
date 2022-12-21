import numpy as np

A = np.array([[2,1],[5,3]])
b = np.array([10,13])

result = np.linalg.solve(A,b)
print(result)