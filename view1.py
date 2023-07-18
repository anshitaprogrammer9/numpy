import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view();
arr[1]=20;
print(x);
print(arr);

arr1=np.array([1,2,3,4,5,6,7,8])
y=arr1.view();
y[1]=313;
print(arr1)
print(y)