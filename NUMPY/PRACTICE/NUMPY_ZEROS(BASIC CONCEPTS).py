#shape is compulsory
#remember default datatype is float
#by providing just shape
#by default order is C but there is another one which is F
import numpy as np
zero=np.zeros(5)
print(zero)
print()

#by providing shape and  data type
zero=np.zeros(5,"int")
print(zero)
print()

#by providing two dimensions in shape with tuple
zero=np.zeros((2,3))
print(zero)
print()

#by providing two dimensions in shape with list
zero=np.zeros([2,3],"int")
print(zero)
print()

#by providing order as well
zero=np.zeros([2,4],order="F")
print(zero)