import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape of array:", arr.shape)

reshaped_arr = arr.reshape(3, 2)
print("Reshaped array:\n", reshaped_arr)
