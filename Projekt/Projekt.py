import tkinter as tk
from random import *

root = tk.Tk()
root.geometry("900x500")
root.configure(bg="#d4f1f9")


value = tk.StringVar(value="")
text = tk.Label(root, textvariable=value,
                font=("Times New Roman", 30), 
                bg="#d4f1f9")
text.pack(pady=20)

frame = tk.Frame(root)
frame.pack(expand=True)


button1 = tk.Button(
                    frame,
                    text="1",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "1"))

button2 = tk.Button(
                    frame,
                    text="2",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "2"))

button3 = tk.Button(
                    frame,
                    text="3",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "3"))

button4 = tk.Button(
                    frame,
                    text="4",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "4"))

button5 = tk.Button(
                    frame,
                    text="5",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "5"))

button6 = tk.Button(
                    frame,
                    text="6",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "6"))

button7 = tk.Button(
                    frame,
                    text="7",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "8"))

button8 = tk.Button(
                    frame,
                    text="8",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "8"))

button9 = tk.Button(
                    frame,
                    text="9",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "9"))


button_s = tk.Button(
                    frame,
                    text="_",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + " "))

button0 = tk.Button(
                    frame,
                    text="0",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get() + "0"))

button_b = tk.Button(
                    frame,
                    text="<",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    command=lambda: value.set(value.get()))


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
