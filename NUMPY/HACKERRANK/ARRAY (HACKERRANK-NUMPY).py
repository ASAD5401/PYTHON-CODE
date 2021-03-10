import numpy
def arrays(arr):
    l=[eval(i) for i in arr]
    q=l[::-1]
    w=numpy.array(q,dtype="f")
    return w
arr = input().strip().split(' ')
result = arrays(arr)
print(result)