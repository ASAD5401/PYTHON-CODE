#by providing just no of rows which is N
import numpy as np
ey=np.eye(5)
print(ey)
print()

#by providing just no of rows which is N and no of columns which ix M
ey=np.eye(2,3)
print(ey)
print()

#by providing N and negative diagonal which is k
ey=np.eye(4,k=-1)
print(ey)
print()

#by providing N and positive diagonal which is k
ey=np.eye(5,k=2)
print(ey)
print()

#by providing N and datatype
ey=np.eye(4,dtype="int")
print(ey)
print()