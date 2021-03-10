import numpy as np
s=str(input()).split()
l=[int(i) for i in s]
a=np.array(l)
b=np.reshape(a,(3,3))
print(b)