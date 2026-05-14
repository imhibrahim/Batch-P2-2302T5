import tkinter as tk
from tkinter import messagebox
root =tk.Tk()
root.geometry("400x500")
root.title("My Python Window Application")

heading=tk.Label(root,text="Simple Calculator",font=("arial",14,"bold italic") ,fg="Green")
heading.pack(pady=12)



def submit():
    global num1,num2

    try:
        num1=int(inp1.get())
        num2=int(inp2.get())
        messagebox.showinfo("Submitted","user input is saved")
    except ValueError:
        messagebox.showerror('Input Error',"Please Insert the input values")
   


def add():
    result=num1+num2
    lable.config(text=f"Result : {result}")
     
def sub():
    result=num1-num2
    lable.config(text=f"Result Is : {result}")

def mul():
    result=num1*num2
    lable.config(text=f"Result Is : {result}")
def divid():
    result=num1/num2
    lable.config(text=f"Result Is : {result}")
    


inp1=tk.Entry(root,width=40)
inp2=tk.Entry(root,width=40)
inp1.pack(pady=10)
inp2.pack(pady=10)

submit=tk.Button(root,text="Submit",command=submit)
submit.pack(pady=13)

btn_group=tk.Frame(root)
btn_group.pack()


tk.Button(btn_group,text="Addition",width=12,command=add).grid(row=0,column=0,padx=5,pady=5)
tk.Button(btn_group,text="Subtraction",width=12, command=sub).grid(row=0,column=1,padx=5,pady=5)
tk.Button(btn_group,text="Multiply",width=12,command=mul).grid(row=1,column=0,padx=5,pady=5)
tk.Button(btn_group,text="Divid",width=12,command=divid).grid(row=1,column=1,padx=5,pady=5)


lable=tk.Label(root,text="Result : ", font=("arial",14,"bold"), fg="blue")
lable.pack(pady=14)

root.mainloop()


