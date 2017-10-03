import requests
import json

api_key = "59ecb95e623a2b6c"

r = requests.get("http://api.wunderground.com/api/" + api_key + "forecast/q/France/Pars.json")

data = r.json()

for day in data['forecast']['simpleforecast']['forecastday']:
    print(day['date']['weekday'] + ":")
    print("Conditions: ", day['conditions'])
    print("High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C")

