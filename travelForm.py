from tkinter import *

def getVals():
    print("Submitted.")
    with open("records.txt", "a") as f:
        f.write(f"{name.get(), num.get(), gender.get(), emergencyNum.get(), paymentMode.get(), meals.get()}")
        f.write("\n")
    name.set("")
    num.set("")
    gender.set("")
    emergencyNum.set("")
    paymentMode.set("")
    meals.set(NO)

root = Tk()
root.geometry("320x200")
root.minsize(320, 200)
root.maxsize(320, 200)
root.title("Travel Form")

# Packed Labels to Display On Screen
Label(root, text="Welcome to Rohit Travels",  font="comicsansms 13 bold").grid(row=0, column=1)
Label(text="Name").grid(row=1, column=0)
Label(text="Phone No.").grid(row=2, column=0)
Label(text="Gender").grid(row=3, column=0)
Label(text="Emergency No.").grid(row=4, column=0)
Label(text="Payment Mode").grid(row=5, column=0)

#Variables
name = StringVar()
num = StringVar()
gender= StringVar()
emergencyNum = StringVar()
paymentMode = StringVar()
meals = IntVar()

#Entries for the form
Entry(root, textvariable=name).grid(row=1, column=1)
Entry(root, textvariable=num).grid(row=2, column=1)
Entry(root, textvariable=gender).grid(row=3, column=1)
Entry(root, textvariable=emergencyNum).grid(row=4, column=1)
Entry(root, textvariable=paymentMode).grid(row=5, column=1)
Checkbutton(text="Wanna have your meals?", variable=meals).grid(row=6, column=1)

# Submit Button
Button(text="Submit", command=getVals).grid(row=7, column=1)

root.mainloop()