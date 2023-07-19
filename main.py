import random
import tkinter as tk

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
        result_label.config(text='You win!')

    return win

def check_guess():
    guess = entry.get()
    w = comp(num4, guess)
    if not w and attempts.get() >= 10:
        result_label.config(text='You lose!')
    attempts.set(attempts.get() + 1)
    entry.delete(0, tk.END)

num4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(num4)
num4 = num4[:4]

root = tk.Tk()
root.title('Number Guessing Game')

instructions_label = tk.Label(root, text='Enter 4 numbers:')
instructions_label.pack()

entry = tk.Entry(root, width=10)
entry.pack()

attempts = tk.IntVar()
attempts.set(1)

check_button = tk.Button(root, text='Check', command=check_guess)
check_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
