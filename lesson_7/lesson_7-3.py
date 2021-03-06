import datetime
import requests

URL='http://api.openweathermap.org/data/2.5/forecast/daily'
any_days = int(input('Введите колличество дней: '))
def return_weather(days=1):
    data = {'q' : 'Odesa','cnt' : days, 'units':'metric','appid':'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()
result = return_weather(any_days)
print('\tдата\t\t\tтемпература днем\tТемпература ночью\tПо ощущениям днем\tПо ощущениям ночью')
for day in result['list']:
    date = day['dt']
    print(datetime.datetime.fromtimestamp(date).strftime("%d-%m-%Y"), '\t', '\t', '\t', '\t', day['temp']['day'],'\t', '\t',  '\t', '\t', day['feels_like']['day'],'\t' '\t', '\t', '\t', '\t',
         day['temp']['night'],'\t' '\t', '\t', '\t', day['feels_like']['night'] )

print(datetime.datetime.today())
namefile = str(datetime.datetime.today().strftime("%d-%m-%Y")) + '-Odesa-' + str(any_days) + '-days-weather-forecast.txt'
with open(namefile, 'w', encoding = 'utf-8') as f:
    f.write('Дата\t\tTемпература днем\tПо ощущениям днем\tТемпература ночью\tПо ощущениям ночью\n')
    for day in result['list']:
        date = day['dt']
        f.write(str(datetime.datetime.fromtimestamp(date).strftime("%d-%m-%Y")) + '\t\t\t\t' +
                     str(day['temp']['day']) + '\t\t\t\t' + str(day['feels_like']['day']) + '\t\t\t\t\t' +
         str(day['temp']['night']) + '\t\t\t\t' + str(day['feels_like']['night']) + '\n')