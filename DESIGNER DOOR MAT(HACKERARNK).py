x=str(input()).split()
n=int(x[0])
m=int(x[1])
a=int(n/2)
for i in range(1,n,2):
    print(((".|.")*i).center(m,"-"))
print(("WELCOME").center(m,"-"))
for i in range(n-2,0,-2):
    print(((".|.") * i).center(m, "-"))