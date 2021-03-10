a=int(input("enter value of matrix x 1*1"))
b=int(input("enter value of matrix x 1*2"))
c=int(input("enter value of matrix x 2*1"))
d=int(input("enter value of matrix x 2*2"))
e=int(input("enter value of matrix y 1*1"))
f=int(input("enter value of matrix y 1*2"))
g=int(input("enter value of matrix y 2*1"))
h=int(input("enter value of matrix y 2*2"))
x=[[a,b],[c,d]]
y=[[e,f],[g,h]]
z=[[0,0],[0,0]]
z[0][0]=(a*e+b*g)
z[0][1]=(a*f+b*h)
z[1][0]=(c*e+d*g)
z[1][1]=(c*f+d*h)
print("[",z[0][0],"\t",z[0][1],"]")
print("[",z[1][0],"\t",z[1][1],"]")