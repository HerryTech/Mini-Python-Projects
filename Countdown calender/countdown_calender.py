from tkinter import *
from datetime import date, datetime

window = Tk()
canvas = Canvas(window, width = 800, height = 800, bg = "black")
canvas.pack()
canvas.create_text(100, 50, anchor = "w", fill = "orange", font= "Arial 28 bold underline", text ="Holidays countdown calender")
window.mainloop()

def get_events():
    list_events = []
    filename = "Countdown calender\event.txt"
    with open(filename) as f:
        for line in f:
            line = line.strip("\n")
            current_event = line.split(",")
            print(current_event)
        
get_events()