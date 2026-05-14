import tkinter as tk
root =tk.Tk()


root.geometry("400x500")
root.title("My Python Window Application")


head1=tk.Label(root,text="Welcome To Project",font=("arial",13),fg="Brown")
head1.pack(pady=13)

def getvalue():
    label1=tk.Label(root,text=inp1+inp2.get())

    label1.pack(pady=10)

inp1=tk.Entry(root,width=30)
inp1.pack(pady=14)


btn1=tk.Button(root,text="Submit",font=("arial",14),fg="yellow",bg="black",command=getvalue)
btn1.pack(pady=10)












# text=tk.Label(root,text="My New Site for Python",fg="green",bg="lightblue",font=("Algerian",20))
# text.pack()

# btn=tk.Button(root,text="Submit",fg="white",bg="black",font=("Arial",13,"bold italic"))
# btn.pack()


root.mainloop()


