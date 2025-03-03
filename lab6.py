## 💡 Exercise 1: Why is NumPy Faster?
# 🔹 Write a Python program in PyCharm that compares the speed of Python lists vs. NumPy arrays for squaring 1 million numbers.
import numpy as np
import time
n = 1000000
py_list = list(range(n))
np_arr = np.arange(n)
start = time.time()
py_list_sq = list(map(lambda x: x**2, py_list))
end = time.time()
py_list_time = end - start

start = time.time()
np_arr_sq = np_arr ** 2
end = time.time()
np_arr_time = end - start

print(f"Python List Squaring time: {py_list_time} seconds")
print(f"Numpy Array Squaring time: {np_arr_time} seconds")

# 📝 Question: Which approach is faster? Why?
# Numpy is much faster because it uses C implementation, which is faster than Python code. Python is executed line by line,
# which slows down the execution. C translates directly into machine language and is executed immediately.

## 💡 Exercise 2: Create Different Arrays
# 🔹 Create a 4x4 matrix of random numbers.
# 🔹 Print its shape, size, and dimensions.

matrix = np.random.rand(4,4)
print(matrix)
print(f"Matrix Shape: {matrix.shape}")
print(f"Matrix Size: {matrix.size}")
print(f"Matrix dimensions: {matrix.ndim}")

## 💡 Exercise 3: Random Data Generation
# 🔹 Create a 3x3 identity matrix.
# 🔹 Create a 1D array of 20 random integers between 1 and 100.

id_matrix = np.eye(3)
rand_arr = np.random.randint(1,101,20)

print(id_matrix)
print(rand_arr)


## 💡 Exercise 4: Array Slicing

# 🔹 Given a 5x5 matrix of numbers from 1 to 25, extract:
# The third row
# The last two columns
# A 3x3 submatrix from the center

matrix = np.arange(1,26).reshape(5,5)
third_row = matrix[2, :]
last_two = matrix[:, -2:]
center_sub = matrix[1:4, 1:4]
print("5x5 matrix:\n", matrix)
print("Third row:\n", third_row)
print("Last two:\n", last_two)
print("Center Submatrix:\n", center_sub)

## 💡 Exercise 5: Reshaping Practice
# 🔹 Reshape a 1D array of 20 elements into a 4x5 matrix.

arr_twenty = np.random.randint(1,100,20)
print("Original array:\n", arr_twenty)
matrix_twenty = arr_twenty.reshape(4,5)
print("Reshaped array:\n", matrix_twenty)
