import numpy as np

"""

Poniżej znajduje sie funkcja licząca wyznacznik macierzy, 
która wykorzystywana jest w funkcji wyznaczającej rząd macierzy.

"""



#definicja macierzy z zadania

matrixA = np.array([[1, 1, 5],
                   [2, 0, 6],
                   [8, 3, 2]])

matrixB = np.array([[3, -1, 1],
                    [5, 1, 4],
                    [-1, 3, 2]])

matrixC = np.array([[1, 3, -1, 4],
                    [1, -1, 4, 5],
                    [0, 1, 4, -2],
                    [10, -2, 5, 1]])

matrixD = np.array([[2, 8, 3, -4],
                    [1, 4, 1, -2],
                    [5, 20, 0, -10],
                    [-3, -12, -2, 6]])

# funkcja licząca rząd macierzy

def det(matrix, r):
        if r == 1:
            return matrix[0][0]
        elif r == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            determinant = 0
            for j in range(len(matrix[0])):
                smaller_matrix = []
                for i in range(1, len(matrix)):
                    row = []
                    for k in range(len(matrix[i])):
                        if k != j:
                            row.append(matrix[i][k])
                    smaller_matrix.append(row)
                determinant += ((-1) ** j) * matrix[0][j] * det(smaller_matrix, r - 1)
            return determinant

def matrix_rank(matrix):
    
    rank = 0
    wymiary = len(matrix)

    for r in range(1, wymiary + 1):
        determinant = det(matrix, r)
        if determinant != 0:
            rank = r
        else:
            break

    return rank



        

print(f"Moja funkcja: {matrix_rank(matrixA)}, funkcja linalg.matrix_rank(): {np.linalg.matrix_rank(matrixA)}")
print(f"Moja funkcja: {matrix_rank(matrixB)}, funkcja linalg.matrix_rank(): {np.linalg.matrix_rank(matrixB)}")
print(f"Moja funkcja: {matrix_rank(matrixC)}, funkcja linalg.matrix_rank(): {np.linalg.matrix_rank(matrixC)}")
print(f"Moja funkcja: {matrix_rank(matrixD)}, funkcja linalg.matrix_rank(): {np.linalg.matrix_rank(matrixD)}")




