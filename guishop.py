from tkinter import*
from tkinter import messagebox
l=list()
def hellmet():
    l.append(2000)
def stumps():
    l.append(3000)
def bat():
    l.append(10000)
def keeping():
    l.append(2500)
def caps():
    l.append(300)
def jersey():
    l.append(1000)
def ball():
    l.append(500)
def shoes():
    l.append(2000)
def trouser():
    l.append(1000)
def pads():
    l.append(1500)
def guard():
    l.append(500)
def thigh():
    l.append(1000)
def band():
    l.append(200)
def kitbag():
    l.append(3000)
def gloves():
    l.append(500)
def checkout():
    z = sum(l)



    o=len(l)
    v.config(text=z)
    v1.config(text=o)
def BILL():
    z=sum(l)
    p = int(l20.get())
    if (p >= z):
        q = p - z
        v2.config(text=q)
    else:
        messagebox.showinfo("invalid amount")

m=Tk()
m.title("SHOPPING APPLICATION")
l1=Checkbutton(m,text="HELLMET",bg="yellow",fg="red",width=18,font=("Arial",16),command=hellmet).grid(row=1,column=1,padx=5,pady=5)
a=PhotoImage(file=r"E:hellmet.png")
img1=a.subsample(2,2)
I1=Label(m,image=img1).grid(row=2,column=1)
l2=Checkbutton(m,text="GLOVES",bg="yellow",fg="red",width=18,font=("Arial",16),command=gloves).grid(row=3,column=1,padx=5,pady=5)
b=PhotoImage(file=r"E:glove.png")
img2=b.subsample(2,2)
I2=Label(m,image=img2).grid(row=4,column=1)
l3=Checkbutton(m,text="PADS",bg="yellow",fg="red",width=18,font=("Arial",16),command=pads).grid(row=5,column=1,padx=5,pady=5)
c=PhotoImage(file=r"E:pad.png")
img3=c.subsample(2,2)
I3=Label(m,image=img3).grid(row=6,column=1)
L4=Checkbutton(m,text="STUMPS",bg="yellow",fg="red",width=18,font=("Arial",16),command=stumps).grid(row=1,column=2,padx=5,pady=5)
d=PhotoImage(file=r"E:stump.png")
img4=d.subsample(2,2)
I4=Label(m,image=img4).grid(row=2,column=2)
l5=Checkbutton(m,text="JERSEY",bg="yellow",fg="red",width=18,font=("Arial",16),command=jersey).grid(row=3,column=2,padx=5,pady=5)
e=PhotoImage(file=r"E:jersey.png")
img5=e.subsample(2,2)
I5=Label(m,image=img5).grid(row=4,column=2)
l6=Checkbutton(m,text="GUARD",bg="yellow",fg="red",width=18,font=("Arial",16),command=guard).grid(row=5,column=2,padx=5,pady=5)
f=PhotoImage(file=r"E:guar.png")
img6=f.subsample(2,2)
I6=Label(m,image=img6).grid(row=6,column=2)
l7=Checkbutton(m,text="BAT",bg="yellow",fg="red",width=18,font=("Arial",16),command=bat).grid(row=1,column=3,padx=5,pady=5)
g=PhotoImage(file=r"E:bat.png")
img7=g.subsample(2,2)
I7=Label(m,image=img7).grid(row=2,column=3)
l8=Checkbutton(m,text="BALL",bg="yellow",fg="red",width=18,font=("Arial",16),command=ball).grid(row=3,column=3,padx=5,pady=5)
h=PhotoImage(file=r"E:ball.png")
img8=h.subsample(2,2)
I8=Label(m,image=img8).grid(row=4,column=3)
l9=Checkbutton(m,text="THIGH PAD",bg="yellow",fg="red",width=18,font=("Arial",16),command=thigh).grid(row=5,column=3,padx=5,pady=5)
i=PhotoImage(file=r"E:thigh.png")
img9=i.subsample(2,2)
I9=Label(m,image=img9).grid(row=6,column=3)
l10=Checkbutton(m,text="KEEPING GLOVES",bg="yellow",fg="red",width=18,font=("Arial",16),command=keeping).grid(row=1,column=4,padx=5,pady=5)
j=PhotoImage(file=r"E:keeping.png")
img10=j.subsample(2,2)
I10=Label(m,image=img10).grid(row=2,column=4)
l11=Checkbutton(m,text="SHOES",bg="yellow",fg="red",width=18,font=("Arial",16),command=shoes).grid(row=3,column=4,padx=5,pady=5)
k=PhotoImage(file=r"E:shoe.png")
img11=k.subsample(2,2)
I11=Label(m,image=img11).grid(row=4,column=4)
l12=Checkbutton(m,text="BANDS",bg="yellow",fg="red",width=18,font=("Arial",16),command=band).grid(row=5,column=4,padx=5,pady=5)
y=PhotoImage(file=r"E:bands.png")
img12=y.subsample(2,2)
I12=Label(m,image=img12).grid(row=6,column=4)
l13=Checkbutton(m,text="CAPS",bg="yellow",fg="red",width=18,font=("Arial",16),command=caps).grid(row=1,column=5,padx=5,pady=5)
p=PhotoImage(file=r"E:cap.png")
img13=p.subsample(2,2)
I13=Label(m,image=img13).grid(row=2,column=5)
l14=Checkbutton(m,text="TROUSERS",bg="yellow",fg="red",width=18,font=("Arial",16),command=trouser).grid(row=3,column=5,padx=5,pady=5)
n=PhotoImage(file=r"E:trouser.png")
img14=n.subsample(2,2)
I14=Label(m,image=img14).grid(row=4,column=5)
l15=Checkbutton(m,text="KIT BAG",bg="yellow",fg="red",width=18,font=("Arial",16),command=kitbag).grid(row=5,column=5,padx=5,pady=5)
o=PhotoImage(file=r"E:kit.png")
img15=o.subsample(2,2)
I15=Label(m,image=img15).grid(row=6,column=5)
l16=Button(m,text="CHECKOUT",bg="yellow",fg="red",width=18,font=("Arial",16),command=checkout).grid(row=7,column=1,padx=5,pady=5)
l17=Label(m,text="Your total bill is:",bg="yellow",fg="red",width=18,font=("Arial",16)).grid(row=9,column=1,padx=5,pady=5)
l18=Label(m,text="Your no of items are:",bg="yellow",fg="red",width=18,font=("Arial",16)).grid(row=8,column=1,padx=5,pady=5)
l19=Label(m,text="Amount Paid:",bg="yellow",fg="red",width=18,font=("Arial",16)).grid(row=10,column=1,padx=5,pady=5)
l20=Entry(m,bg="yellow",fg="red",width=18,font=("Arial",16))
l20.grid(row=10,column=2,padx=5,pady=5)
v=Label(m,bg="yellow",fg="red",font=("Arial",16),width=20,bd="5")
v.grid(row=9,column=2,padx=10,pady=10)
v1=Label(m,bg="yellow",fg="red",font=("Arial",16),width=20,bd="5")
v1.grid(row=8,column=2,padx=10,pady=10)
l21=Label(m,text="Cash Back:",bg="yellow",fg="red",width=18,font=("Arial",16)).grid(row=11,column=1,padx=5,pady=5)
v2=Label(m,bg="yellow",fg="red",font=("Arial",16),width=20,bd="5")
v2.grid(row=11,column=2,padx=10,pady=10)
l21=Button(m,text="BILL",bg="yellow",fg="red",width=18,font=("Arial",16),command=BILL).grid(row=7,column=3,padx=5,pady=5)
m.mainloop()