import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8])
for x in arr:
    print(x)
print("**************")
arr1=np.array([[1,2,3],[4,5,67]])
for y in arr1:
    for x in y:
        print(x)

arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in arr2:
    print(i)
print("*********")
for a in arr2:
    for b in a:
        print(b)
print("*********")
for j in arr2:
    for k in j:
        for l in k:
            print(l)