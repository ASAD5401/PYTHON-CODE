import cmath
def quad(a,b,c):
    s1=(-b+cmath.sqrt(b*b-4*a*c))/2*a
    s2=(-b-cmath.sqrt(b*b-4*a*c))/2*a
    return s1,s2
a=eval(input("enter constant term of x*x:"))
b=eval(input("enter constant term of x:"))
c=eval(input("enter constant term:"))
result=quad(a,b,c)
print("the solution set is",result)