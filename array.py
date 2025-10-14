# changing the index of an numpy array
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
arr[0] = 1000
print(arr)

# changing the shape of a numpy array
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr = arr.reshape(3, 2)
print(reshaped_arr)


# creat a 4by4 matrix and the extarct the even rows and odd columns
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
extracted = matrix[::2, 1::2]
print(extracted) 