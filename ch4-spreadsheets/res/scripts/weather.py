import requests
import csv
import json

from datetime import date, timedelta

one_day = timedelta(days=1)
fmt = "%Y%m%d"
outfmt = "%Y-%m-%d"
d = date(2016, 1, 1)

url = "http://api.wunderground.com/api/59ecb95e623a2b6c/history_"
station = "/q/airport/kbji.json"

daily = [
        'meantempm',
        'maxtempm',
        'mintempm',
        'meanpressurem',
        'maxpressurem',
        'minpressurem',
        'humidity',
        'maxhumidity',
        'minhumidity',
        'precipm',
        ]

fieldnames = list(daily)
fieldnames.append('date')

with open('weather.csv', 'a') as f:
    fieldnames = daily
    fieldnames.append('date')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

for i in range(366):
    
    r = requests.get(url + d.strftime(fmt) + station)

    data = r.json()
    with open('weather.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        line = {}
        for i in range(len(daily)):
            line[daily[i]] = data['history']['dailysummary'][0][daily[i]]
        line['date'] = d.strftime(outfmt)
        writer.writerow(line)

    d = d + one_day
    print(d.strftime(outfmt))
