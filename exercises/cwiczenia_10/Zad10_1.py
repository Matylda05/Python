import tkinter as tk
from random import *

root = tk.Tk()
root.geometry("900x500")
root.configure(bg="#d4f1f9")

kostka = tk.Label(root, text=" ",
                font=("Times New Roman", 100, "bold"), 
                bg="#d4f1f9")
kostka.pack(pady=50)


button = tk.Button(root,
                   text="Rzuć kością",
                   font=("Times New Roman", 30, "bold"),
                   bg="#9ae2f5",
                   fg="black",
                   activebackground="#0590b5",
                   activeforeground="black",
                   command=lambda: kostka.config(text=randrange(1, 7)))
button.pack(pady=50)

root.mainloop()
