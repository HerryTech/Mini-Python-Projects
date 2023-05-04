from requests import get
import json

url = "https://restcountries.com/v3.1/all"

r = get(url)
response = r.json()
filename = "Ask the expert/countries.json"
with open(filename, "w") as f:
    json.dump(response, f, indent = 4)

#countries = response.name 
#for country in 

#print(response[1]["name"]["common"])

print(len(response))
#print(response.items)
