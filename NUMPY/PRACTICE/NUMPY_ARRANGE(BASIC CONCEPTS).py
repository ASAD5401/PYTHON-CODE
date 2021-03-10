#arrange (start,stop,step,dtype=none)

#by providing start and end
import numpy as np
arr=np.arange(1,11)
print(arr)
print()

#by providing end only
import numpy as np
arr=np.arange(3)
print(arr)
print()

#by providing start end & step
arr=np.arange(1,10,2)
print(arr)
print()

#by providing stop & datatype
arr=np.arange(10,dtype="complex")
print(arr)
print()

#by providing start stop step & dtype
arr=np.arange(1,20,5,"float")
print(arr)