import numpy as np
arr=np.array([1,2,3,4,5,6,8,13])
x=arr.copy();
y=arr.view();
print(x.base);
print(y.base);