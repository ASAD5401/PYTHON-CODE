import sqlite3
from tkinter import*
from tkinter import messagebox

conn = sqlite3.connect('myfirst.sqlite')
cur = conn.cursor()
cur.executescript('CREATE TABLE IF NOT EXISTS STUDENTDB (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,NAME    TEXT UNIQUE,MARKS   INTEGER)')
m=Tk()
#image ko png mn convert karne ke bad online ico mn bhi convert karen ge
m.iconbitmap('E:\\MYFIRSTDATABASE.ico')
m.configure(bg="gray60")
m.title("STUDENT DATABASE")
t1=Label(m,text="ENTER NEW RECORD",bg="gray30",fg="red",font=("Arial",16),width=18,bd="5")
t1.grid(row=0,column=0,padx=5,pady=5)
v1=Label(m,text="NAME :",bg="gray45",fg="red",font=("Arial",16),width=18,bd="5")
v1.grid(row=1,column=0,padx=5,pady=5)
op1=Entry(m,bg="gray47",fg="red",width=8,font=("Arial",16),bd="5")
op1.grid(row=1,column=1,padx=5,pady=5)
v2=Label(m,text="MARKS :",bg="gray45",fg="red",font=("Arial",16),width=18,bd="5")
v2.grid(row=2,column=0,padx=5,pady=5)
op2=Entry(m,bg="gray47",fg="red",width=8,font=("Arial",16),bd="5")
op2.grid(row=2,column=1,padx=5,pady=5)
def submit():
    x=op1.get()
    y=op2.get()
    cur.execute('''INSERT INTO STUDENTDB (NAME,MARKS) VALUES (?,?)''', (x, int(y)))
    conn.commit()
    op1.delete(0,END)
    op2.delete(0,END)
    messagebox.showinfo("SUBMIT SUCCESSFULLY",f"One new record inserted \n Name : {x} \n Marks : {y}")
submit=Button(m,text="SUBMIT",bg="gray47",fg="red",width=8,font=("Arial",16),bd="5",command=submit)
submit.grid(row=3,column=0,padx=5,pady=5)


t2=Label(m,text="DELETE RECORD",bg="gray30",fg="red",font=("Arial",16),width=18,bd="5")
t2.grid(row=4,column=0,padx=5,pady=10)
v2=Label(m,text="NAME :",bg="gray45",fg="red",font=("Arial",16),width=18,bd="5")
v2.grid(row=5,column=0,padx=5,pady=5)
op3=Entry(m,bg="gray47",fg="red",width=8,font=("Arial",16),bd="5")
op3.grid(row=5,column=1,padx=5,pady=5)
def delete():
    x=op3.get()
    cur.execute('''DELETE FROM STUDENTDB WHERE NAME=?''', (x,))
    conn.commit()
    op3.delete(0,END)
    messagebox.showinfo("DELETE SUCCESSFULLY", f"One record deleted \n Name : {x}")
delete=Button(m,text="DELETE",bg="gray47",fg="red",width=8,font=("Arial",16),bd="5",command=delete)
delete.grid(row=6,column=0,padx=5,pady=5)

t3=Label(m,text="UPDATE RECORD",bg="gray30",fg="red",font=("Arial",16),width=18,bd="5")
t3.grid(row=0,column=3,padx=5,pady=10)
v1=Label(m,text="NAME :",bg="gray45",fg="red",font=("Arial",16),width=18,bd="5")
v1.grid(row=1,column=3,padx=5,pady=5)
op4=Entry(m,bg="gray47",fg="red",width=8,font=("Arial",16),bd="5")
op4.grid(row=1,column=4,padx=5,pady=5)
v2=Label(m,text="MARKS :",bg="gray45",fg="red",font=("Arial",16),width=18,bd="5")
v2.grid(row=2,column=3,padx=5,pady=5)
op5=Entry(m,bg="gray47",fg="red",width=8,font=("Arial",16),bd="5")
op5.grid(row=2,column=4,padx=5,pady=5)
def update():
    x=op4.get()
    y=op5.get()
    cur.execute('''UPDATE STUDENTDB SET MARKS=? WHERE NAME=?''',(y,x))
    conn.commit()
update=Button(m,text="UPDATE",bg="gray47",fg="red",width=8,font=("Arial",16),bd="5",command=update)
update.grid(row=3,column=3,padx=5,pady=5)



m.mainloop()
