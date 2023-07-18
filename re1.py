import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr=arr.reshape(4,3)
print(newarr)
new1 = arr.reshape(2, 3, 2)

print(new1)
new2 = arr.reshape(3, 2, 2)

print(new2)
print(arr.reshape(2,6).base)

newarr1 = arr.reshape(2, 2, -1);
print(newarr1)
print("****************")
arr5 = np.array([[1, 2, 3], [4, 5, 6]])

newarr5 = arr5.reshape(-1)
print(newarr5)