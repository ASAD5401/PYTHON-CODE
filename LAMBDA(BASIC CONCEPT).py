a=lambda x:x+x
b=a(5)
print(b)

a=lambda x,y:x*y
b=a(2,3)
print(b)

a=[0,1,2,3,4,5,6,7,8,9]
b=map(lambda x:x+x,a)
print(list(b))

