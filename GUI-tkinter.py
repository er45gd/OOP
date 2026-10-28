import tkinter as Tk
from tkinter import *

top = Tk()

top.geometry("500x500")

answer = Text(width=35,height=2)
answer.place(x=100, y=50)

def show(x):
    try:
        if x=="=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(Tk.INSERT, x)
            answer.insert(Tk.INSERT, final_answer)
        else:
            answer.insert(Tk.INSERT, x)

    except:
        answer.delete(1.0.END)


B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
B1.place(x=100, y=100)

B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=200, y=100)

B3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
B3.place(x=300, y=100)

B4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
B4.place(x=100, y=200)

B5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
B5.place(x=200, y=200)

B6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
B6.place(x=300, y=200)

B7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
B7.place(x=100, y=300)

B8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
B8.place(x=200, y=300)

B9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
B9.place(x=300, y=300)

B0 = Button(top, text="0", width=10, height=5, command=lambda: show("0"))
B0.place(x=200, y=400)

top.mainloop()