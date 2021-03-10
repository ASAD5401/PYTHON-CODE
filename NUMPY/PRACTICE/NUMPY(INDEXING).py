#1 dimensional array
import numpy as np
a=np.array([1,2,3,4])
print(a[2])
print(a[-1])
print()

# 2 dimensional array
a=np.array([[1,2],[3,4]])
print(a[1][0])
#There is negative indexing in 2d array as well but first we can only focus on positive indexing

#3 dimensional array
a=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(a.shape)
print(a[0][2][2])
print(a[1][1][1])
print(a[1][2][0])