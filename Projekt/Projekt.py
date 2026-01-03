import tkinter as tk
from random import *

root = tk.Tk()
root.geometry("900x500")
root.configure(bg="#d4f1f9")


value_const = tk.StringVar(value="")
value = tk.StringVar(value="")

text = tk.Label(
    root,
    font=("Times New Roman", 30),
    bg="#d4f1f9"
)
text.pack(pady=20)

def refresh_label():
    text.config(text=value_const.get() + value.get())

frame = tk.Frame(root)
frame.pack(expand=True)

B_WIDTH = 6
B_HEIGHT = 1

def wpisz(x):
    value.set(value.get() + x)
    refresh_label()

button1 = tk.Button(
                    frame,
                    text="1",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("1")
                    )

button2 = tk.Button(
                    frame,
                    text="2 abc",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("2")
                    )

button3 = tk.Button(
                    frame,
                    text="3 def",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("3")
                    )

button4 = tk.Button(
                    frame,
                    text="4 ghi",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("4")
                    )

button5 = tk.Button(
                    frame,
                    text="5 jkl",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("5")
                    )

button6 = tk.Button(
                    frame,
                    text="6 mno",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("6")
                    )

button7 = tk.Button(
                    frame,
                    text="7 pqrs",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("7")
                    )

button8 = tk.Button(
                    frame,
                    text="8 tuv",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("8")
                    )

button9 = tk.Button(
                    frame,
                    text="9 wxyz",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("9")
                    )

def spacja():
    value_const.set(value_const.get() + value.get() + " ")
    value.set("")
    refresh_label()

button_s = tk.Button(
                    frame,
                    text="_",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=spacja)

button0 = tk.Button(
                    frame,
                    text="0",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("0")
                    )

def backspace():
    if value.get() == "":
        value_const.set(value_const.get()[:-1])
        refresh_label()
    else:
        value.set(value.get()[:-1])
        refresh_label()


button_b = tk.Button(
                    frame,
                    text="<",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: backspace()
                    )


button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=1, column=2, padx=5, pady=5)
button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
button7.grid(row=3, column=0, padx=5, pady=5)
button8.grid(row=3, column=1, padx=5, pady=5)
button9.grid(row=3, column=2, padx=5, pady=5)
button_s.grid(row=4, column=0, padx=5, pady=5)
button0.grid(row=4, column=1, padx=5, pady=5)
button_b.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
