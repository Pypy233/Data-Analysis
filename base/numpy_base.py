import numpy as np
import json

data1 = [0, -1.2, 3.3, 10.2]
arr1 = np.array(data1)
print(arr1)
print(arr1.dtype)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.dtype)

print(np.zeros(10))
print(np.zeros((3, 6)))
print(np.empty((2, 3, 2)))
print(np.arange(20))

arr = np.array([1, 2, 3, 4, 5])
print(arr1.dtype)
trans_arr = arr.astype(np.float64)
print(trans_arr)
print(trans_arr.dtype)

arr = np.arange(10)
print(arr[5:8])
arr[5:8] = 12
print(arr)
