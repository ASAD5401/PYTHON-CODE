
import tkinter
from tkinter import messagebox

m=tkinter.Tk()
def hello():
    messagebox.showinfo("HELLO,your dats is here",stdid.get()+"\n",stdname.get()+"\n",stdaddress.get()+"\n",)
l1=tkinter.label(m,text="Student- ID",bg="yellow",fg="red",font=("Arial",16)).grid(row=0,column=0,paddy=5)
l2=tkinter.label(m,text="Student- NAME",bg="yellow",fg="red",font=("Arial",16)).grid(row=1,column=0,paddy=5)
l3=tkinter.label(m,text="Student- ADDRESS",bg="yellow",fg="red",font=("Arial",16)).grid(row=2,column=0,paddy=5)
l4=tkinter.label(m,text="GENDER",bg="yellow",fg="red",font=("Arial",16)).grid(row=3,column=0,paddy=5)
img=tkinter.PhotoImage(file=r"path of file.png")

img
stdid=tkinter.Entry(m).grid(row=0,column=1,paddy=5)
stdname=tkinter.Entry(m).grid(row=1,column=1,paddy=5)
stdaddress=tkinter.Entry(m).grid(row=2,column=1,paddy=5)
c1=tkinter.checkbutton(m,text="MALE",bg="yellow",fg="red",font=("Arial",16)).grid(row=3,COLUMN=1,PADDY=5)
c2=tkinter.checkbutton(m,text="FEMALE",bg="yellow",fg="red",font=("Arial",16)).grid(row=4,COLUMN=1,PADDY=5)
m.mainloop()