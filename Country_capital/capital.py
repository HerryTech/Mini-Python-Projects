from requests import get
from tkinter import Tk, simpledialog, messagebox, Canvas
import json

query_country = simpledialog.askstring("Country", "Type the name of a country:")
name = query_country

url = f"https://restcountries.com/v3.1/name/{name}"
r = get(url)
response = r.json()
filename = "Country_capital/country.json"
with open(filename, "w") as f:
    json.dump(response, f, indent = 4)

with open(filename) as f:
    country = json.load(f)

capital = country[0]["capital"][0]
         
messagebox.showinfo("Answer", f"The capital city of {name} is {capital}")
#window = Tk()


#window.mainloop()

