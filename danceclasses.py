from tkinter import *

def collect_data():
    with open("data.txt", "a") as f:
        f.write(name.get())
        f.write(" : ")
        f.write(num.get())
        f.write("\n")
        print(f"Name : {name.get()}\nNumber : {num.get()}")


root = Tk()
root.geometry("655x333")
root.title("Dance Class Form")

user = Label(root, text="Enter your name : ")
ph_no = Label(root, text="Enter your number : ")
user.grid(row=0, column=0)
ph_no.grid(row=1, column=0)

name = StringVar()
num = StringVar()

nameEntry = Entry(root, textvariable=name)
numEntry = Entry(root, textvariable=num)
nameEntry.grid(row=0, column=1)
numEntry.grid(row=1, column=1)

Button(text="Submit", command=collect_data).grid(pady=10)


root.mainloop()