from tkinter import *
import tkinter.messagebox as tmsg

def rate():
    print(value.get())
    with open("ratings.txt", "a") as f:
        f.write(str(value.get()))
        f.write("\n")
    tmsg.showinfo("Have a nice day.", "Thanks for rating us.")
    value.set(0)
root = Tk()
root.geometry("400x200")
root.title("Rating")
value = IntVar()
Label(root, text="Please rate us from (0-10)")
sliderVal = Scale(root, from_=0, to=10,orient=HORIZONTAL, variable=value).pack()
Button(text="Submit", command=rate).pack()


root.mainloop()