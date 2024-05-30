# wektory

import numpy as np

my_vector1 = np.array([1, 2, 3, 4, 5])
print("My vector: ", my_vector1)

my_vector2 = np.arange(5)
my_vector3 = np.arange(0, 10, 2)

print("My vector: ", my_vector2)
print("My vector: ", my_vector3)

my_vector4 = np.linespace(1, np.pi, 4)

new_vector = np.append(my_vector4, [1000])
print("New vector with 1000 at the end: ", new_vector)

my_vector4 = np.arange(5)
new_vector_instert = np.insert(my_vector4, 1, 8888)
print("Vector with value 8888 at index 1: ", new_vector_instert)

arr = np.array([1, 2, 3, 4, 5])
index = 0
arr2 = np.delete(arr, index)
print("Based array: ", arr, "Arrey with removed value[0]: ", arr2)

vec1 = np.array([1, 2, 3, 4, 5])
vec2 = np.array([5, 4, 3, 2, 1])

subtract1 = np.subtract(vec1, vec2)
subtract2 = vec1 - vec2

print("After subtracting using function: ", subtract1)
print("After subtracting without function: ", subtract2)

vec1 = np.array([1, 2, 3, 4, 5])
vec2 = np.array([0, 2, 3, 0, 2])

multiply1 = np.multiply(vec1, vec2)
multiply2 = vec1 * vec2

print("After multipled using function: ", multiply1)
print("After multipled without function: ", multiply2)

vec1 = np.array([1, 2, 3, 4, 15])
vec2 = np.array([0, 4, 9, 0, 10])

divide1 = np.divide(vec1, vec2)
divide2 = vec1 * vec2

print("After divided using function: ", divide1)
print("After divided without function: ", divide2)


# macierze


matrix1 = np.array([[1, 2, 3, 4, 15], [2, 4, 6, 8, 10]])
print(matrix1)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)
print(x)

m = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)
x = np.matrix(m)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)

first_value = x[0][0]
middle_value = x[1][1]
last_value = x[-1][-1]

print("first element in matrix", first_value)
print("middle element in matrix", middle_value)
print("last element in matrix", last_value)

a = np.diag((1, 2, 3, 4))
print(a)

zeros = np.zeros((3, 3))
print(zeros)

ones = np.ones((3, 3))
print(ones)

x = zeros.copy()
x[0][2] = 6
print(x)

# tensory

import tensorflow as tf

t1 = tf.constant([1, 2, 3])
t2 = tf.constant([[1.1, 2.2, 3.3], [4, 5, 6]])
t3 = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t4 = tf.constant(["String_one", "String_two", "String_three"])

print(t1)
print("")
print(t2)
print("")
print(t3)
print("")
print(t4)


