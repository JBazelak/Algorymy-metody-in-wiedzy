import numpy as np

A = np.array([2, 1, 1, 1, 3, 6, 4, 5, 5]).reshape(3, 3)
B = np.array([1, 0, 5, 2, 1, 6, 0, 3, 0]).reshape(3, 3)
C = np.dot(A, B)

print("Mnożenie za pomocą np.dot() \n", C)

D = np.matmul(A, B)
E = A @ B

print("Mnożenie za pomocą np.matmul() \n", D)
print("Mnożenie za pomocą operatora @ \n", E)

A = np.array([[6, 1, 1, 4],
              [4, -2, 5, 1],
              [2, 8, 7, 4],
              [2, 2, 1, 3]])

print("Rank of A: ", np.linalg.matrix_rank(A))

A + np.array([[6, 1, 1],
              [4, -2, 5],
             [2, 8, 7]])

print("\nDeterminant of A:", np.linalg.det(A))

A = np.array([[4, 3, 2, 0],
              [-4, -2, -5, 1],
              [12, 8, -7, 4]])

M = np.transpose(A)
print(M)