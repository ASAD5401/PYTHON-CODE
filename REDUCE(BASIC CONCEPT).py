import functools
num=[1,2,3,4,5,6,7]
print(functools.reduce(lambda x,y:x+y,num))