from tkinter import *
from datetime import date, datetime

window = Tk()
canvas = Canvas(window, width = 800, height = 800, bg = "black")
canvas.pack()
canvas.create_text(100, 50, anchor = "w", fill = "orange", font= "Arial 28 bold underline", text ="Holidays countdown calender")
window.mainloop()