import numpy as np 
arr=np.array([1,2,3,4,5])
x=np.where(arr==4)
print(x)
y=np.where(arr%2==0)
print("Even numbers :",y)
z=np.where(arr%2!=0)
print("ODD Number :",z)
a=np.where(arr%2!=0)
print("ODD Number :",a)
b=np.searchsorted(arr,3)
print(b)