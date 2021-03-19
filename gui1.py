#to find the sub,subtract,multiply of 2 nos. using tkinter (GUI)means mini calculator
from tkinter import *
def sum():
    a=float(ea.get())
    b=float(eb.get())
    c=a+b
    ans.set("Sum : "+str(c))
def sub():
    a=float(ea.get())
    b=float(eb.get())
    c=a-b
    ans.set("Subtract : "+str(c))
def mul():
    a=float(ea.get())
    b=float(eb.get())
    c=a*b
    ans.set("Multiply : "+str(c))
window=Tk()
window.title("Mini Calculator")
window.geometry("600x500")
la=Label(window,text="Value of A : ",font=("Arial",10),fg="red")
la.place(x=50,y=50)
ea=Entry(window,fg="blue" ,font=("Arial",10))
ea.place(x=130,y=50)

lb=Label(window,text="Value of B : ",font=("Arial",10),fg="red")
lb.place(x=50,y=100)
eb=Entry(window,fg="blue" ,font=("Arial",10))
eb.place(x=130,y=100)

b1=Button(window,text="+",width="8" ,fg="Blue",font=("arial",15),command=sum)
b1.place(x=70,y=200)

b2=Button(window,text="-",width="8" ,fg="Blue",font=("arial",15),command=sub)
b2.place(x=180,y=200)

b3=Button(window,text="*",width="8" ,fg="Blue",font=("arial",15),command=mul)
b3.place(x=290,y=200)
ans=StringVar()
lans=Label(window,font=("Arial",13),fg="red",textvariable=ans)
lans.place(x=90,y=150)
window.mainloop()
