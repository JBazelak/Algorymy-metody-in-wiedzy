import numpy as np

print("====ZAD 2====")

def multiply_matrices(matrix1, matrix2):
    #przypasanie wymiarów macierzy do zmiennych w celu późniejszego sprawdzenia czy macierze można pomnożyć
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    # Sprawdzenie, czy można pomnożyć macierze(liczba kolumn w pierwszej macierzy musi być równa liczbie wierszy w drugiej macierzy)
    if cols1 != rows2:
        print("Nieprawidłowe wymiary macierzy dla mnożenia")

    # Inicjalizacja pustej macierzy wynikowej
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Mnożenie macierzy
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Przykładowe macierze
matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix_B = [[7, 8], [9, 10], [11, 12]]

# Wywołanie funkcji mnożącej macierze
result_matrix = multiply_matrices(matrix_A, matrix_B)

# Wydruk wyniku
for row in result_matrix:
    print(row)



print("====ZAD 2 ====")


def det(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3:
        raise ValueError("Macierz musi być wymiaru 3x3")

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det

# Przykładowa macierz 3x3
matrix= [[1, 4, 5], [2, 1, 6], [0, 3, 2]]

# Wywołanie funkcji
result = det(matrix)

print("Wyznacznik macierzy 3x3:")
print(result)


print("====ZAD 3 ====")


def transpose(matrix):
    # Pobranie liczby wierszy i kolumn
    rows, cols = len(matrix), len(matrix[0])

    # Sprawdzenie, czy macierz jest pusta
    if len(rows) == 0 or len(cols) == 0:
        return []

    # Transpozycja macierzy
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix

# macierz z zadania
matrix = [[3, 2, 4, 1, 8, 0], [2, 3, 5, 6, 0, 3], [7, 7, 2, 1, 4, 5]]

# Wywołanie funkcji
transposed_matrix = transpose(matrix)

# Wydruk wyniku
for row in transposed_matrix:
    print(row)