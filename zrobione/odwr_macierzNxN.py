import numpy as np



def multiply(matrix1, matrix2):
    result = np.zeros((matrix1.shape[0], matrix2.shape[1]))

    for i in range(matrix1.shape[0]):
        for j in range(matrix2.shape[1]):
            for k in range(matrix2.shape[0]):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
   
    return result

def inverse(matrix):
    # Utworzenie macierzy jednostkowej
    n = len(matrix)
    identity = np.eye(n)

    # Skopiowanie macierzy, aby nie modyfikować oryginalnej
    copyMain = np.copy(matrix).astype(float)  # Zmiana typu danych na float
    copyIdentity = np.copy(identity).astype(float)

    # Eliminacja Gaussa-Jordana
    for i in range(n):
        # Wyznaczenie diagonalnego elementu
        wartosc = copyMain[i][i]
        
        # Skalowanie wiersza, aby diagonalny element był równy 1
        copyMain[i] /= wartosc
        copyIdentity[i] /= wartosc

        # Eliminacja elementów
        for j in range(n):
            if j != i:
                factor = copyMain[j][i]
                copyMain[j] -= factor * copyMain[i]
                copyIdentity[j] -= factor * copyIdentity[i]

    return copyIdentity, copyMain

# Macierz do odwrócenia
matrix = np.array([[8, 1, 4, 2, 1],
                   [8, 6, 4, 2, 1],
                   [1, 2, 3, 4, 1],
                   [8, 0, 6, 2, 5],
                   [1, 9, 6, 4, 1]])

I = np.eye(5)

# Odwrócenie macierzy
inverse_matrix, modifiedMain = inverse(matrix)

# Wyświetlenie wyniku
print("Macierz odwrotna:")
print(inverse_matrix)

# Sprawdzenie poprawności wyniku
print("\nSprawdzenie poprawności:\n")

print("Funkcja numpy:\n")
print(np.linalg.inv(matrix))

print("\nZmodyfikowana macierz glowna\n")
print(modifiedMain)

print("\nPrzemnozenie macierzy oryginalnej z odwrocona")
print(multiply(matrix, inverse_matrix))

#dodakowo skożystałem z funkcji allclose która sprawdza czy odwrotność jest poprawna

print("\nFunkcja allclose")
if np.allclose(multiply(matrix, inverse_matrix), I):
    print("Odwrotnosc macierzy jest poprawna.")
else:
    print("Odwrotnosc macierzy jest niepoprawna.")