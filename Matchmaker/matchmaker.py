from random import shuffle
from tkinter import Tk, Button, DISABLED

root = Tk()
root.title('Matchmaker')
root.resizable(width = False, height = False)

buttons = {}
button_symbols = {}
symbols = [chr(9986), chr(128383), chr(9989), chr(128393), chr(8987), chr(128194), chr(9997), chr(9996), chr(128077), chr(128078), chr(128528), chr(9992), chr(10065), chr(10066)]

shuffle(symbols)

for i in range(6):
    for j in range(4):
        button = Button(command = lambda i = i, j = j : show_symbol(i, j), width = 3, height = 3)
        button.grid(column = i, row = j)
        buttons[i, j] = button
        button_symbols[i, j] = symbols.pop()

#root.mainloop()