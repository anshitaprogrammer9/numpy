import numpy as np 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2));
arrrq=np.stack((arr1,arr2))
arrrn=np.hstack((arr1,arr2))

ard=np.dstack((arr1,arr2))
print("&&")
print(ard);
print("&&")
ar=np.vstack((arr1,arr2))
print("********")
print(ar)
print("***********")
print(arrrn)
print(arrrq)
print(arr)
arr3=np.array([[1,2,3],[4,5,6]])
arr4=np.array([[7,8,9],[10,11,12]])
arrr=np.concatenate((arr3,arr4),axis=1);
print(arrr)