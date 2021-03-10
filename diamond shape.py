for i in range(5):
    print((" ")*(5-i-1)+"* "*(i+1))
for j in range(5-1,0,-1):
    print(" "*(5-j)+"* "*j)


for i in range(5):
    print("*"*i)

print( )
for i in range(5):
    print("*"*(5-i))
print()
for i in range(5):
    print((" "*(5-i))+("*"*i))
print()
for i in range(5):
    print((" "*i)+"*"*(5-i))
print()
l=["1","3","6"]
print(l)
n=list(map(int,l))
print(n)