import requests
city = "Moscow,RU"
appid = "74583c60efe5f5d40eef966210a60992"

#погода в данный момент
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Город:", city)
print("Скорость ветра: ", data['wind']['speed'], 'm/s')
print("Видимость: ", data['visibility'], 'm')

#погода на неделю
res7 = requests.get("http://api.openweathermap.org/data/2.5/forecast",  params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data7 =res7.json()

print('\n')
print("Прогноз погоды на неделю: ")
for i in data7['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <", '{0:+3.0f}'.format(i['wind']['speed']), "> \r\nВидимость <", '{0:+3.0f}'.format(i['visibility']), ">")
    print("____________________________")