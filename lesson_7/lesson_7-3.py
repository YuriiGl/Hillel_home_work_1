import requests
URL='http://api.openweathermap.org/data/2.5/forecast/daily'
def return_weather(days=1):
    data = {'q' : 'Odesa','cnt' : days, 'units':'metric','appid':'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()
result = return_weather(days = 3)
def write_file():
    print()
print('температура днем\tТемпература ночью\tПо ощущениям днем\tПо ощущениям ночью')
#print(result)
for day in result['list']:
   print(day['temp']['day'],'\t', '\t', '\t',  '\t', '\t', day['feels_like']['day'],'\t' '\t', '\t', '\t', '\t',
         day['temp']['night'],'\t' '\t', '\t', '\t', '\t', day['feels_like']['night'] )
print('done')

import datetime
print(datetime.datetime.today())