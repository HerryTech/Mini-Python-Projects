from tkinter import *
from datetime import date, datetime

window = Tk()
canvas = Canvas(window, width = 800, height = 800, bg = "black")
canvas.pack()
canvas.create_text(100, 50, anchor = "w", fill = "orange", font= "Arial 28 bold underline", text ="Holidays countdown calender")

def get_events():
    list_events = []
    list = []
    filename = "Countdown calender\event.txt"
    with open(filename) as f:
        for line in f:
            line = line.strip("\n")
            current_event = line.split(",")
            event_date = datetime.strptime(current_event[1], "%d/%m/%y").date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events
      
def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(" ")
    return number_of_days[0]
      
events = get_events()
events.sort(key = lambda x: x[1])
today = date.today()

vertical_space = 100

for event in events:
    event_name = event[0]
    days_until_event = days_between_dates(event[1], today)
    display = f"It's {days_until_event} days until {event_name}"
    canvas.create_text(100, vertical_space, anchor = "w", fill = "white", font = "Arial 12 bold", text = display)
    vertical_space += 50

window.mainloop()
