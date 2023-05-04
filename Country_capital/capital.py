from requests import get
from tkinter import simpledialog, messagebox, Canvas
import json

while True:
    query_country = simpledialog.askstring("Country", "Type the name of a country:")
    name = query_country.capitalize()

    url = f"https://restcountries.com/v3.1/name/{name}"
    r = get(url)
    if r.status_code != 200:
        messagebox.showerror("Error", "Not a valid country")
    else:
        response = r.json()
        filename = "Country_capital/country.json"
        with open(filename, "w") as f:
            json.dump(response, f, indent = 4)

        with open(filename) as f:
            country = json.load(f)

        capital = country[0]["capital"][0]
         
        messagebox.showinfo("Answer", f"The capital city of {name} is {capital}")


