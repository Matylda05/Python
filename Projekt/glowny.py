import tkinter as tk
import slownik as sl

def find(sequence):
    result = []
    for word in sl.slownik_words:
        if len(word) != len(sequence):
            continue

        podobny = True
        for num, litera in zip(sequence, word):
            if num not in sl.t9 or litera not in sl.t9[num]:
                podobny = False
                break

        if podobny:
            result.append(word)

    return result

root = tk.Tk()
root.geometry("1500x900")
root.configure(bg="#d4f1f9")


words = []  
current_word = ""
wyszukane_slowa = []
wypisz_slownik = "Slownik: "
pointer = 0
cursor_visible = True

B_WIDTH = 6
B_HEIGHT = 1


text = tk.Label(
    root,
    text = "|",
    font=("Times New Roman", 30),
    bg="#d4f1f9"
)
text.grid(row=0, column=0, columnspan=2, pady=20)

frame = tk.Frame(root)
frame.grid(row=1, column=0, padx=20, sticky="n")

wypisny_slownik = tk.Label(
    root,
    text= wypisz_slownik,
    font=("Times New Roman", 30),
    bg="#d4f1f9"
)
wypisny_slownik.grid(row=1, column=1, sticky="nw")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

def refresh():
    if cursor_visible:
        text.config(text="".join(words + [current_word]) + "|")
    else:
        text.config(text="".join(words + [current_word]) + " ")

def update_wybrane_slowo():
    global wypisz_slownik
    if not wyszukane_slowa:
        wypisz_slownik = "Slownik: Brak slow"
    else:
        tab = []
        for i, word in enumerate(wyszukane_slowa):
            if i == pointer:
                tab.append(f"[{word}]") 
            else:
                tab.append(word)
        wypisz_slownik = "Slownik: " + " , ".join(tab)
    
    wypisny_slownik.config(text=wypisz_slownik)

def wpisz(x):
    global current_word
    current_word += x
    refresh()

def spacja():
    global current_word
    words.append(current_word + " ")
    current_word = ""
    refresh()

def backspace():
    global current_word 

    if current_word:
        current_word = current_word[:-1]
    elif words:
        current_word = words.pop()
        current_word = current_word[:-1] 
    refresh()

def left():
    global pointer
    if not wyszukane_slowa:
        return
    
    if pointer == 0:
        pointer = len(wyszukane_slowa) - 1
    else:
        pointer = pointer-1
    update_wybrane_slowo()

def wybierz():
    global current_word, wyszukane_slowa
    if not wyszukane_slowa:
        return
    
    current_word = wyszukane_slowa[pointer]
    words.append(current_word)
    current_word = ""
    wyszukane_slowa = []
    refresh()
    update_wybrane_slowo()

def right():
    global pointer
    if not wyszukane_slowa:
        return
    
    if pointer == len(wyszukane_slowa)-1:
        pointer = 0
    else:
        pointer = pointer+1
    update_wybrane_slowo()

def predict():
    global wypisz_slownik, wyszukane_slowa, pointer
    wyszukane_slowa = find(current_word)
    pointer = 0
    update_wybrane_slowo()

def blink_cursor():
    global cursor_visible
    cursor_visible = not cursor_visible
    refresh()
    root.after(500, blink_cursor)


button1 = tk.Button(
                    frame,
                    text="1 sym",
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

button_left= tk.Button(
                    frame,
                    text="\u2190",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=3,
                    height=B_HEIGHT,
                    command=lambda: left()
                    )

button_wybierz= tk.Button(
                    frame,
                    text="wybierz",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wybierz()
                    )

button_right= tk.Button(
                    frame,
                    text="\u2192",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=3,
                    height=B_HEIGHT,
                    command=lambda: right()
                    )

button_T9= tk.Button(
                    frame,
                    text="wyszukaj slowo",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    height=B_HEIGHT,
                    command=lambda: predict()
                    )

button_g = tk.Button(
                    frame,
                    text="*",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("*"))

button_h = tk.Button(
                    frame,
                    text="#",
                    font=("Times New Roman", 30, "bold"),
                    bg="#9ae2f5",
                    fg="black",
                    activebackground="#0590b5",
                    activeforeground="black",
                    width=B_WIDTH,
                    height=B_HEIGHT,
                    command=lambda: wpisz("#"))

button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=1, column=2, padx=5, pady=5)
button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
button7.grid(row=3, column=0, padx=5, pady=5)
button8.grid(row=3, column=1, padx=5, pady=5)
button9.grid(row=3, column=2, padx=5, pady=5)
button_g.grid(row=4, column=0, padx=5, pady=5)
button0.grid(row=4, column=1, padx=5, pady=5)
button_h.grid(row=4, column=2, padx=5, pady=5)

button_s.grid(row=5, column=1, padx=5, pady=5)
button_b.grid(row=5, column=2, padx=5, pady=5)

button_T9.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

button_left.grid(row=7, column=0, padx=5, pady=5)
button_wybierz.grid(row=7, column=1, padx=5, pady=5)
button_right.grid(row=7, column=2, padx=5, pady=5)


blink_cursor()

root.mainloop()
