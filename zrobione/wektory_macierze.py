#zad 1
print("==== ZAD 1 ====")
import numpy as np
import tensorflow as tf
vector = np.array([1, 4, 5, 6, 2, 1, 5, 6, 7, 0])
print("Vector - Zad 1")
print(vector)
#a

index = 5
_del = np.delete(vector, index)
print("1.a")
print(_del)
#b

_add = np.append(vector, 8)
print("1.b")
print(_add)

#c

niep = np.array([1, 4, 5, 6, 2, 1, 5, 6, 7, 0])
for i in range(len(niep)):
    if niep[i] % 2 != 0:
        niep[i] += 2
print("1.c")
print(niep)
#d

rev = vector[::-1]
print("1.d")
print(rev)
print(vector)

#zad 2
print("==== ZAD 2 ====")
wektor_numpy = np.array([1, 2, 3, 4, 5])
lista = [1, 2, 3, 4, 5]
skalar = 3

wynik_numpy = skalar * wektor_numpy
wynik_lista = skalar * lista

print("Wektor numpy:", wektor_numpy)
print("Wynik mnożenia wektora numpy przez skalar:", wynik_numpy)
print("\nLista:", lista)
print("Wynik mnożenia listy przez skalar:", wynik_lista)

odp = "\nMnożenie wektora numpy przez skalar powoduje że każdy jego element zostanie odpowiednio przemnożony\n" \
      "natomiast mnożenie powoduje powielenie elementów listy w zaleznosci od wartości skalara"

print(odp)

print("==== ZAD 3 ====")

# zad 3

matrix = np.array([[3, 5, 0],[2, 6, 1],[3, 8, 9]])
print(matrix)

# 3.a

matrix[0, 0] = -2
print("\n3.a")
print(matrix)

# 3.b

matrix[2, 2] = 44

print("\n3.b")
print(matrix)

matrix[2, 2] = 0

print("\n3.c")
print(matrix)

print("==== ZAD 4 ====")


paz = np.array([[3, 5, 0],[2, 6, 1],[3, 8, 9]])

for i in range(paz.shape[0]):
    for j in range(paz.shape[1]):
        if paz[i, j] % 2 == 0:
            paz[i, j] = 0

print(paz)


print("==== ZAD 5 ====")

#5
matrix_a = np.array([2, 1, 1, 1, 3, 6, 4, 5, 5]).reshape(3, 3)
matrix_b = np.array([1, 0, 5, 2, 1, 6, 0, 3, 0]).reshape(3, 3)
matrix_c = np.zeros((3, 3))

for i in range(matrix_a.shape[0]):
    for j in range(matrix_a.shape[1]):
        matrix_c[i, j] = matrix_a[i, j] + matrix_b[i, j]

print("")
print(matrix_c)
print("")

print("==== ZAD 6 ====")



t1 = tf.constant([1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2])

print("Dane tensora:")
print("Ranga: 2, Kształt: Kwadrat, Rozmiar 4x4 ")
