import numpy as np
arr=np.array([1,2,4,5,6,78,9,36,46,35,233])
print(arr[:5])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr1[1, 1:4])
print(arr1[0:2, 2])
print(arr1[0:2, 1:4])