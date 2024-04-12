import numpy as np

"""

Poniższy kod rozwiązuje układy równań metodą Cramera.
Aby otrzymać rozwiązanie musimy przekazać funkcji
solveEquations() macierz która zawiera stałe wartości
wystepujace przy niewiadomych oraz szereg rozwiązań równań
(wartości znajdujące sie za znakiem "=")

Czyli jeżeli mamy równanie

x + 2y + 3z = 5
3x + 2y + z = 4

(analogicznie do późniejszych deklaracji pierwszy argument zadeklrujemy nastepująco)

matrixC = np.array([1, 2, 3],
                    3, 2, 1)

a drugi argument

valuesC = [5, 4]

"""
matrixA = np.array([[3, 5],
                    [1, 4]])

matrixB = np.array([[1, 2, 3],
                    [3, 1, -3],
                    [-3, 4, 7]])



valuesA = [-7, 14]
valuesB = [-5, 4, -7]


def copyMatrix(matrix):
    copied_matrix = np.empty_like(matrix)  
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            copied_matrix[i, j] = matrix[i, j]  
    return copied_matrix


def det(matrix):
    
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        
        for j in range(len(matrix)):
            smallerMatrix = []
            for i in range(1, len(matrix)):
                row = []
                for k in range(len(matrix[i])):
                    if k != j:
                        row.append(matrix[i][k])
                smallerMatrix.append(row)
            determinant += ((-1) ** j) * matrix[0][j] * det(smallerMatrix)
    return determinant

def solveEquations(matrix, consts):
    result = []
    det_D = det(matrix)

    for i in range(len(matrix)):
        # print("iteracja: " , i)
        temporaryMatrix = copyMatrix(matrix)
        # print(temporaryMatrix)
        for j in range(len(matrix)):
            # print("wew iter: ", j)
            temporaryMatrix[j][i] = consts[j]
            # print(temporaryMatrix)
        det_Di = det(temporaryMatrix)
        result.append(det_Di / det_D)
    return result


print("Macierz A")
print(solveEquations(matrixA, valuesA))
print("Macierz B")
print(solveEquations(matrixB, valuesB))


print("===FUNKCJE NUMPY===")
print("a")
print(np.linalg.solve(matrixA, valuesA))
print("b")
print(np.linalg.solve(matrixB, valuesB))