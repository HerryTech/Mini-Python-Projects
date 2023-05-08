from random import shuffle
from tkinter import Tk, Button, DISABLED
import time

root = Tk()
root.title('Matchmaker')
root.resizable(width = False, height = False)

buttons = {}
first_in_the_match = True
previousI = 0
previousJ = 0
button_symbols = {}

symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708', u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B', u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']

shuffle(symbols)

for i in range(6):
    for j in range(4):
        button = Button(command = lambda i = i, j = j : show_symbol(i, j), width = 10, height = 5)
        button.grid(column = i, row = j)
        buttons[i, j] = button
        button_symbols[i, j] = symbols.pop() 
   
def show_symbol(i, j):
    global first_in_the_match
    global previousI
    global previousJ
    buttons[i, j]["text"] = button_symbols[i, j]
    buttons[i, j].update_idletasks()
    
    if first_in_the_match:
        previousI = i
        previousJ = j
        first_in_the_match = False
    elif previousI != i or previousJ != j:
        if buttons[previousI, previousJ]["text"] != buttons[i, j]["text"]:
            time.sleep(0.5)
            buttons[previousI, previousJ]["text"] = ""
            buttons[i, j]["text"] = ""
        else:
            buttons[previousI, previousJ]["command"] = DISABLED
            buttons[i, j]["command"] = DISABLED
        first_in_the_match = True
    

root.mainloop()