

import numpy as np
s=str(input())
s=s.split()
a=int(s[0])
b=int(s[1])
c=int(s[2])
ar1=np.ones((a,c),dtype="int32")
ar2=np.ones((b,c),dtype="int32")
for i in range(a):
    l = list()
    s=str(input())
    q=s.split()
    for j in q:
       l.append(int(j))
    ar1[i]=l
for i in range(b):
    l = list()
    s=str(input())
    q=s.split()
    for j in q:
       l.append(int(j))
    ar2[i]=l
print(np.concatenate((ar1,ar2),axis=0))