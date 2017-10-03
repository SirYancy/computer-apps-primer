import requests
import json

api_key = "59ecb95e623a2b6c"

r = requests.get("http://api.wunderground.com/api/59ecb95e623a2b6c/history_20160405/q/airport/kbji.json")

data = r.json()

print(data)
