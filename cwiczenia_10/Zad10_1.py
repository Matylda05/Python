import tkinter as tk
import random

root = tk.Tk()
root.title("Rzut Kostką")
root.geometry("1500x900")

kostka = random(6)
label = tk.Label(root, text=kostka)
label.pack(pady=10)


button = tk.Button(root, text="Rzuć kością")
button.pack()


root.mainloop()