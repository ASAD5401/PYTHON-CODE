z=0
from math import*
def a():
    op1.insert()
def add():
    x=op1.get()
    y=op2.get()
    z=eval(x)+int(y)
    v.config(text=z)
def sub():
    x=op1.get()
    y=op2.get()
    z=eval(x)-int(y)
    v.config(text=z)
def mul():
    x=op1.get()
    y=op2.get()
    z=eval(x)*int(y)
    v.config(text=z)
def div():
    x=op1.get()
    y=op2.get()
    z=eval(x)/int(y)
    v.config(text=z)

from math import*

def lg():
    x = eval(op1.get())
    z = log10(x)
    v.config(text=z)
def l():
    x = eval(op1.get())
    z = log(x)
    v.config(text=z)
def SN():
    x=eval(op1.get())
    z=asin(x)
    v.config(text=z)
def CS():
    x=eval(op1.get())
    z=acos(x)
    v.config(text=z)
def TN():
    x=eval(op1.get())
    z=atan(x)
    v.config(text=z)
def fact():
    fact=eval(op1.get())
    for i in range(1,fact):
        fact=fact*i
    v.config(text=fact)
def sn():
    x=eval(op1.get())
    z=sin(x)
    v.config(text=z)
def cs():
    x=eval(op1.get())
    z=cos(x)
    v.config(text=z)
def tn():
    x=eval(op1.get())
    z=tan(x)
    v.config(text=z)
def root():
    x=eval(op1.get())
    z=sqrt(x)
    v.config(text=z)
def clr():
    x=int(op1.get())
    op1.delete(0,x)
def one():
    op1.insert(0,1)
def two():
    op1.insert(0,2)
def three():
    op1.insert(0,3)
def four():
    op1.insert(0,4)
def five():
    op1.insert(0,5)
def six():
    op1.insert(0,6)
def seven():
    op1.insert(0,7)
def p():
    op1.insert(0,3.142)
def eight():
    op1.insert(0,8)
def nine():
    op1.insert(0,9)
def zero():
    op1.insert(0,0)
def power():
    x=int(op1.get())
    y=int(op2.get())
    z=x**y
    v.config(text=z)
from tkinter import*
m=Tk()
m.title("CALCULATOR")
m.resizable(0,0)
l1=Button(m,text="7",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=seven).grid(row=0,column=0,padx=5,pady=5)
l2=Button(m,text="8",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=eight).grid(row=0,column=1,padx=5,pady=5)
l3=Button(m,text="9",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=nine).grid(row=0,column=2,padx=5,pady=5)
l4=Button(m,text="4",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=four).grid(row=1,column=0,padx=5,pady=5)
l5=Button(m,text="5",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=five).grid(row=1,column=1,padx=5,pady=5)
l6=Button(m,text="6",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=six).grid(row=1,column=2,padx=5,pady=5)
l7=Button(m,text="1",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=one).grid(row=2,column=0,padx=5,pady=5)
l8=Button(m,text="2",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=two).grid(row=2,column=1,padx=5,pady=5)
l9=Button(m,text="3",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=three).grid(row=2,column=2,padx=5,pady=5)
l10=Button(m,text="0",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=zero).grid(row=3,column=0,padx=5,pady=5)
l11=Button(m,text="!",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=fact).grid(row=3,column=1,padx=5,pady=5)
l12=Button(m,text="ROOT",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=root).grid(row=4,column=3,padx=5,pady=5)
l13=Button(m,text="/",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=div).grid(row=0,column=3,padx=5,pady=5)
l14=Button(m,text="*",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=mul).grid(row=1,column=3,padx=5,pady=5)
l15=Button(m,text="-",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=sub).grid(row=2,column=3,padx=5,pady=5)
l16=Button(m,text="+",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=add).grid(row=3,column=3,padx=5,pady=5)
l17=Button(m,text="SIN",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=sn).grid(row=4,column=0,padx=5,pady=5)
l18=Button(m,text="COS",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=cs).grid(row=4,column=1,padx=5,pady=5)
l19=Button(m,text="TAN",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=tn).grid(row=4,column=2,padx=5,pady=5)
l20=Button(m,text="x*",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=power).grid(row=3,column=2,padx=5,pady=5)
l21=Button(m,text="SIN-1",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=SN).grid(row=5,column=0,padx=5,pady=5)
l22=Button(m,text="COS-1",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=CS).grid(row=5,column=1,padx=5,pady=5)
l23=Button(m,text="TAN-1",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=TN).grid(row=5,column=2,padx=5,pady=5)
l24=Button(m,text="C",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=clr).grid(row=5,column=3,padx=5,pady=5)
l25=Button(m,text="LOG",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=lg).grid(row=6,column=0,padx=5,pady=5)
l26=Button(m,text="ln",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=l).grid(row=6,column=1,padx=5,pady=5)
l27=Button(m,text="PIE",bg="yellow",width=8,fg="red",font=("Arial",16),bd="5",command=p).grid(row=6,column=2,padx=5,pady=5)
op1=Entry(m,bg="yellow",fg="red",width=8,font=("Arial",16),bd="5")
op1.grid(row=0,column=5,padx=5,pady=5)
op2=Entry(m,bg="yellow",fg="red",width=8,font=("Arial",16),bd="5")
op2.grid(row=1,column=5,padx=5,pady=5)
v=Label(m,bg="yellow",fg="red",font=("Arial",16),width=20,bd="5")
v.grid(row=3,column=5,padx=5,pady=5)
m.mainloop()
