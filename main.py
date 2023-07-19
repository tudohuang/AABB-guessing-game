import random
import tkinter as tk
from tkinter import messagebox

def comp(num4, g4):
    A = 0
    C = 0
    for y in range(4):
        if num4[y] == g4[y]:
            A += 1
        if num4[y] == g4[0] or num4[y] == g4[1] or num4[y] == g4[2] or num4[y] == g4[3]:
            C += 1
    B = C - A
    result_label.config(text='A: {}, B: {}'.format(A, B))
    win = (A == 4)

    if win:
        messagebox.showinfo('Result', 'You win!')
        root.destroy()

    return win

def check_guess():
    guess = entry.get()
    if len(guess) != 4 or not guess.isdigit():
        messagebox.showerror('Error', 'Invalid input! Enter 4-digit number.')
        entry.delete(0, tk.END)
        return
    w = comp(num4, guess)
    if not w and attempts.get() >= 10:
        messagebox.showinfo('Result', 'You lose!')
        root.destroy()
    attempts.set(attempts.get() + 1)
    entry.delete(0, tk.END)

num4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(num4)
num4 = num4[:4]

root = tk.Tk()
root.title('Number Guessing Game')

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#ffffff', bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Arial', 14))
entry.place(relwidth=0.65, relheight=1)

check_button = tk.Button(frame, text='Check', font=('Arial', 12), command=check_guess)
check_button.place(relx=0.7, relheight=1, relwidth=0.3)

attempts = tk.IntVar()
attempts.set(1)

attempts_label = tk.Label(root, text='Attempts: 1', font=('Arial', 14), bg='#ffffff')
attempts_label.place(relx=0.5, rely=0.35, anchor='n')

result_label = tk.Label(root, text='', font=('Arial', 16), bg='#ffffff')
result_label.place(relx=0.5, rely=0.45, anchor='n')

root.mainloop()
