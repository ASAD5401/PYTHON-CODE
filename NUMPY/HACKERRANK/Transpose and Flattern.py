import numpy as np
s=str(input())
s=s.split()
a=int(s[0])
b=int(s[1])
arr=np.ones((a,b),dtype="int32")
for i in range(a):
    l = list()
    s=str(input())
    q=s.split()
    for j in q:
       l.append(int(j))
    arr[i]=l
print(np.transpose(arr))
print(arr.flatten())