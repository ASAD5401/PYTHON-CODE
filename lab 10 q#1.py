import os
w=open("d:\\asad.txt","r")
a=(w.read())
w.close()
s=a.count("\n")
print(s+1)
b=len(a)
print(b)
q=a.split()
print(len(q))
import os
def stats(filename):
    a=open(filename)
    print(len(a.readlines()))
    a.close()
    a = open(filename)
    print(len(a.read()))
    a.close()
    a = open(filename)
    print(len(a.read().split()))
    a.close()
filename=input("Enter name of file that you want to open:")
stats(filename)