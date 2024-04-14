import numpy as np
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

def invMatrix2(matrix):
    detA = det(matrix)
    if detA == 0:
        return "Macierz osobliwa - wyznaczenie macierzy odwrotnej nie mozliwe"
    else:
        a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]
        return (1/detA) * np.array([[d, b],
                                     [-c, a]])


def invMatrix3(matrix):
    detA = det(matrix)
    if detA == 0:
        return "Macierz osobliwa - wyznaczenie macierzy odwrotnej nie mozliwe"
    else:
        wsplDopełnień = np.array([
            [matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1], matrix[0][2]*matrix[2][1] - matrix[0][1]*matrix[2][2], matrix[0][1]*matrix[1][2] - matrix[0][2]*matrix[1][1]],
            [matrix[1][2]*matrix[2][0] - matrix[1][0]*matrix[2][2], matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0], matrix[0][2]*matrix[1][0] - matrix[0][0]*matrix[1][2]],
            [matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0], matrix[0][1]*matrix[2][0] - matrix[0][0]*matrix[2][1], matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]]
            ])
        return (1/detA) * wsplDopełnień

def invMatrix23(matrix):
    if matrix.shape == (2, 2):
        return invMatrix2(matrix)
    elif matrix.shape == (3, 3):
        return invMatrix3(matrix)
    else:
        return "Macierz musi być 2x2 lub 3x3"

matrix1A = np.array([[3, 6],
                   [0, 9]])

matrix1B = np.array([[-3, -9],
                   [1, 3]])

matrix2A = np.array([[1, 0, 5],
                    [2, 7, 6],
                    [8, 3, 2]])

matrix2B = np.array([[3, -1, 1],
                    [5, 1, 4],
                    [-1, 3, 2]])


def printSolution(matrix, nrZad):
    if nrZad[0] == "1":
        print(f'Zadanie {nrZad}:\n Moja funkcja\n {invMatrix2(matrix)}\n')
        try:
            print(f'funkcja numpy\n{np.linalg.inv(matrix)}\n')
        
        except np.linalg.LinAlgError as e:
            print(f'Funkcja numpu:\n Blad podczas wyznaczania odwrotnosci: {e}\n')
    
    elif nrZad[0] == "2":
        
        print(f'Zadanie {nrZad}:\n Moja funkcja\n {invMatrix3(matrix)}\n')
        try:
            print(f'funkcja numpy\n{np.linalg.inv(matrix)}\n')
        except np.linalg.LinAlgError as e:
            print(f'Funkcja numpy\n Blad podczas wyznaczania odwrotnosci: {e}\n')
            
    elif nrZad[0] == "3":
        print(f'Zadanie {nrZad}:\n Moja funkcja\n {invMatrix23(matrix)}\n')
        try:
            print(f'funkcja numpy\n{np.linalg.inv(matrix)}\n')
        except np.linalg.LinAlgError as e:
            print(f'Funkcja numpy\n Blad podczas wyznaczania odwrotnosci: {e}\n')




   


printSolution(matrix1A, "1a")
printSolution(matrix1B, "1b")
printSolution(matrix2A, "2a")
printSolution(matrix2B, "2b")
print("Wyglada na to ze funkcja numpy musi miec blad, obliczalem det na kartce i\n korzystalem z kalkulatora internetowego. Wartosc det zawsze wynosila 0\n tak samo w przypadku mojej funkcji liczącej wyznacznik\n")
printSolution(matrix1A, "3a")
printSolution(matrix1B, "3b")
printSolution(matrix2A, "3c")
printSolution(matrix2B, "3d")

