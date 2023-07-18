import numpy as np 
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]);
for x in np.nditer(arr):
    print(x);
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr1[:, ::2]):
  print(x)
  arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr2):
  print(idx, x)