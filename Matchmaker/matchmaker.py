from random import shuffle
from tkinter import Tk, Button, DISABLED
import time

root = Tk()
root.title('Matchmaker')
root.resizable(width = False, height = False)

buttons = {}
first_in_the_match = True
previousX = 0
previousY = 0
button_symbols = {}

#symbols = [chr(9986), chr(128383), chr(9989), chr(128393), chr(8987), chr(128194), chr(9997), chr(9996), chr(128077), chr(128078), chr(128528), chr(9992), chr(10065), chr(10066)]

symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708', u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B', u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']

shuffle(symbols)

print(symbols)

for i in range(6):
    for j in range(4):
        button = Button(command = lambda i = i, j = j : show_symbol(i, j), width = 3, height = 3)
        button.grid(column = i, row = j)
        buttons[i, j] = button
        button_symbols[i, j] = symbols.pop()
        
def show_symbol(i, j):
    global first_in_the_match
    global previousX
    global previousY
    buttons[i, j]["text"] = button_symbols[i, j]
    buttons[i, j].update_idletasks()
    
    if first_in_the_match:
        previousX = i
        previousY = j
        first_in_the_match = False
    elif previousX != i or previousY != j:
        if buttons[previousX, previousY]["text"] != buttons[i, j]["text"]:
            time.sleep(0.5)
            buttons[previousX, previousY]["text"] = ""
            buttons[i, j]["text"] = ""
        else:
            buttons[previousX, previousY]["command"] = DISABLED
            buttons[i, j]["command"] = DISABLED
        first_in_the_match = True
#root.mainloop()