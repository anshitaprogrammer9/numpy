import numpy as np
arr=np.array(47);
print("0-D ARRAY")
print(arr);
arr1=np.array([1,2,3,4])
print("1-D ARRAY")
print(arr1);
arr2=np.array([[1,2,3],[4,5,6]]);
print("2-D ARRAY")
print(arr2);
arr4=np.array([[[1,2,3],[4,5,6,]],[[7,8,9],[10,11,12]]])
print("3-D ARRAY")
print(arr4)
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr4.ndim)
arr5=np.array([1,2,3,5],ndmin=5);
print(arr5);