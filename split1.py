import numpy as np 
arr=np.array([1,2,3,4,56,7])
arrr=np.array_split(arr,3)
print(arrr[0])
print(arrr[1])
print(arrr[2])
arr1=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
arr2=np.array_split(arr1,3,axis=1)
print("************************")
print(arr2)
print("************************")
ne=np.hsplit(arr1,2)
print(ne)
arr11 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr11, 3)

print(newarr)
