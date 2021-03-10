#by providing start and stop
import numpy as np
lins=np.linspace(2,100)
print(lins)
print()

#by providing start,stop and num
lins=np.linspace(1,100,num=10)
print(lins)
print()

#by providing start,stop and num but in this we use endpoint=false so stop value is not included
lins=np.linspace(1,100,num=4,endpoint=False)
print(lins)
print()

#by providing start,stop and num but in this we use retstep=true so we can also see difference in output
lins=np.linspace(1,100,num=5,retstep=True)
print(lins)
print()

#by default datatype is float but we can change it to int or complex
lins=np.linspace(1,100,num=5,dtype="complex")
print(lins)
print()