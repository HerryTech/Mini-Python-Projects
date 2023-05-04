from requests import get
from tkinter import Tk, simpledialog, messagebox, Canvas
import json

name = "Nigeria"
url = f"https://restcountries.com/v3.1/name/{name}"
r = get(url)
response = r.json()
filename = "Country_capital/country.json"
with open(filename, "w") as f:
    country = json.dump(response, f, indent = 4)

with open(filename) as f:
    country = json.load(f)
         

window = Tk()

window.mainloop()

