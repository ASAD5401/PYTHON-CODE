from math import*
def first(vi,a,t):
    vf=vi+a*t
    return vf
vi=float(input("Enter initial velocity in m/s :"))
a=float(input("Enter acceleration in m*m/s :"))
t=float(input("Enter time in s:"))
result=first(vi,a,t)
print("the final velocity in m/s is:",result)

def second(vi,t,a,):
    s=vi*t+(a*t*t)/2
    return s
vi=float(input("Enter initial velocity in m/s :"))
a=float(input("Enter acceleration in m*m/s :"))
t=float(input("Enter time in s:"))
result=second(vi,t,a)
print("The distance in m is:",result)


def third(vf,vi,a):
    s=((vf*vf)-(vi*vi))/2*a
    return(s)
vi=float(input("Enter initial velocity in m/s :"))
vf=float(input("Enter final velocity in m/s :"))
a=float(input("Enter acceleration in m*m/s :"))
result=third(vf,vi,a)
print("The distance in m is:",result)


