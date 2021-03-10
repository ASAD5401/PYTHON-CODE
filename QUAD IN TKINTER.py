from tkinter import*
from math import*
def quad():
    a=int(l1.get())
    b = int(l2.get())
    c = int(l3.get())
    d1=(-b+sqrt(b*b-4*a*c))/(2*a)
    d2=(-b-sqrt(b*b-4*a*c))/(2*a)
    l.config(text=d1)
    p.config(text=d2)

m=Tk()
l1=Entry(m,bg="yellow",fg="red",bd="5",font=("Arial",16))
l1.grid(row=0,column=0)
l2=Entry(m,bg="yellow",fg="red",bd="5",font=("Arial",16))
l2.grid(row=0,column=1)
l3=Entry(m,bg="yellow",fg="red",bd="5",font=("Arial",16))
l3.grid(row=0,column=2)
l=Label(m,bg="yellow",fg="red",bd="5",font=("Arial",16))
l.grid(row=1,column=0)
p=Label(m,bg="yellow",fg="red",bd="5",font=("Arial",16))
p.grid(row=1,column=1)
b=Button(m,text="QUAD",bg="yellow",fg="red",bd="5",font=("Arial",16),command=quad).grid(row=2,column=0)
m.mainloop()