#1 dimensional array
import numpy as np
a=np.array([1,2,3,4])
print(a[2:4])
print()

# 2 dimensional array
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#making a sub array of 6&7
print(a[1:2,1:3])
#making a sub array of 5,8,9&12
print(a[1:,0::3])
#There is negative indexing in 2d array as well but first we can only focus on positive indexing
print()

#3 dimensional array
a=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
#making an array with 1,4,9,12,13,16,21&24
print(a[:,::2,::3])
print()
#making an array with 18,19,22&23
print(a[1,1:,1:3])