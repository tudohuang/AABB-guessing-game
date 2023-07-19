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
        messagebox.showerror('Error', 'Invalid input! Enter a 4-digit number.')
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
root.geometry('400x300')

title_label = tk.Label(root, text='Number Guessing Game', font=('Arial', 18, 'bold'))
title_label.pack(pady=20)

instruction_label = tk.Label(root, text='Enter a 4-digit number:', font=('Arial', 14))
instruction_label.pack()

entry = tk.Entry(root, font=('Arial', 14), justify='center')
entry.pack(pady=10)

check_button = tk.Button(root, text='Check', font=('Arial', 12), command=check_guess)
check_button.pack(pady=10)

attempts = tk.IntVar()
attempts.set(1)

attempts_label = tk.Label(root, text='Attempts: 1', font=('Arial', 14))
attempts_label.pack()

result_label = tk.Label(root, text='', font=('Arial', 16, 'bold'))
result_label.pack(pady=20)

root.mainloop()
