from requests import get
from tkinter import Tk, simpledialog, messagebox
import json

name = "Nigeria"
url = f"https://restcountries.com/v3.1/name/{name}"
r = get(url)
response = r.json()
filename = "Country_capital/country.json"
with open(filename, "w") as f:
    json.dump(response, f, indent = 4)
    

