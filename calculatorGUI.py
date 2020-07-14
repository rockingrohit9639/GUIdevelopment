from tkinter import *
def click(event):
    global strVal
    text = event.widget.cget("text")
    if text == '=':
        if strVal.get().isdigit():
            value = int(strVal.get())
        else:
            try:
                value = eval(strVal.get())
            except Exception as e:
                value = "Error"
                strVal.set(value)
                screen.update()
                print(e)
        strVal.set(value)
        screen.update()

    elif text == 'C':
        strVal.set("")
        screen.update()
    else:
        strVal.set(strVal.get() + text)
        screen.update()


root = Tk()
root.geometry("410x525")
root.minsize(410, 525)
root.maxsize(410, 525)
root.title("Calculator by Rohit")
root.wm_iconbitmap("1.ico")
strVal = StringVar()
strVal.set("")
screen = Entry(root, font="lucida 30 bold", textvariable=strVal)
screen.pack(padx =5, pady=10, fill=X)

# Frame 1
f1 = Frame(root, bg="gray")
b1 = Button(f1, text="/", padx=20, pady=14, font="lucida 25 bold")
b1.pack(side=LEFT, pady=10, padx=10, fill=BOTH)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="*", padx=20, pady=14, font="lucida 25 bold")
b1.pack(side=LEFT, pady=10, padx=10)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="-", padx=20, pady=14, font="lucida 25 bold")
b1.pack(side=LEFT, pady=10, padx=10)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="+", padx=20, pady=14, font="lucida 25 bold")
b1.pack(side=LEFT, pady=10, padx=10)
b1.bind("<Button-1>", click)

f1.pack(fill=BOTH)


# Frame2
f2 = Frame(root, bg ="grey")
b2 = Button(f2, text="9", padx=16, pady=14, font="lucida 25 bold")
b2.pack(side=LEFT, pady=10, padx=10)
b2.bind("<Button-1>", click)

b2 = Button(f2, text="8", padx=16, pady=14, font="lucida 25 bold")
b2.pack(side=LEFT, pady=10, padx=10)
b2.bind("<Button-1>", click)

b2 = Button(f2, text="7", padx=16, pady=14, font="lucida 25 bold")
b2.pack(side=LEFT, pady=10, padx=10)
b2.bind("<Button-1>", click)

b2 = Button(f2, text="C", padx=16, pady=14, font="lucida 25 bold")
b2.pack(side=LEFT, pady=10, padx=15)
b2.bind("<Button-1>", click)
f2.pack(fill=BOTH)

# Frame 3
f3 = Frame(root, bg="grey")
b3 = Button(f3, text="6", padx=17, pady=14, font="lucida 25 bold")
b3.pack(side=LEFT, pady=15, padx=10)
b3.bind("<Button-1>", click)

b3 = Button(f3, text="5", padx=16, pady=14, font="lucida 25 bold")
b3.pack(side=LEFT, pady=18, padx=10)
b3.bind("<Button-1>", click)

b3 = Button(f3, text="4", padx=16, pady=14, font="lucida 25 bold")
b3.pack(side=LEFT, pady=10, padx=10)
b3.bind("<Button-1>", click)

b3 = Button(f3, text="=", padx=18, pady=14, font="lucida 25 bold")
b3.pack(side=LEFT, pady=10, padx=10)
b3.bind("<Button-1>", click)
f3.pack(fill=BOTH)

# Frame 4
f4 = Frame(root, bg="gray")
b4 = Button(f4, text="3", padx=17, pady=14, font="lucida 25 bold")
b4.pack(side=LEFT, pady=10, padx=10)
b4.bind("<Button-1>", click)

b4 = Button(f4, text="2", padx=17, pady=14, font="lucida 25 bold")
b4.pack(side=LEFT, pady=10, padx=10)
b4.bind("<Button-1>", click)

b4 = Button(f4, text="1", padx=16, pady=14, font="lucida 25 bold")
b4.pack(side=LEFT, pady=10, padx=10)
b4.bind("<Button-1>", click)

b4 = Button(f4, text="0", padx=22, pady=14, font="lucida 25 bold")
b4.pack(side=LEFT, pady=10, padx=10)
b4.bind("<Button-1>", click)
f4.pack(fill=BOTH)



root.mainloop()