from tkinter import *
from datetime import date, datetime

window = Tk()
canvas = Canvas(window, width = 800, height = 800, bg = "black")
canvas.pack()
canvas.create_text(100, 50, anchor = "w", fill = "orange", font= "Arial 28 bold underline", text ="Holidays countdown calender")
#window.mainloop()

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
today = date.today()

for event in events:
    event_name = event[0]
    days_until_event = days_between_dates(event[1], today)
    display = f"It's {days_until_event} days until {event_name}"
    print(display)