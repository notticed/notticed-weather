from config import *
from tokens import *
from coords import *
import requests
from date import *


@app.get("/weather_3d", tags=['weather'])
def weather(res: Response, req: Request):
  weather = []
  city = token.tokens(res, req)['city']
  url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&lang=ru&appid={API_KEY}'
  try:
    r = requests.get(url).json()
    print(r)
    for n in range(0, 5):
      card = r['list'][n]
      date = card['dt_txt'].split(' ')
      day = [str(convert_date(date[0])), convert_time(date[1]), round(kelvin_convert(card['main']['temp']), 1), round(kelvin_convert(card['main']['feels_like']), 2), card['weather'][0]['description'], card['wind']['speed']]
      weather.append(day)
    return weather, city
  except:
    return 'Город не найден'

@app.get("/weather_current", tags=['weather'])
def weather(res: Response, req: Request):
  weather = []
  city = token.tokens(res, req)['city']
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={API_KEY}'
  try:

    r = requests.get(url).json()
    return [str(datetime.fromtimestamp(r['dt'])).split(" ")[0], round(kelvin_convert(r['main']['temp']), 1), kelvin_convert(r['main']['feels_like']), r['weather'][0]['description'], r['wind']['speed']]
  except:
    return 'Город не найден'
  # for n in r:
  #   day = [n['dt_txt'], round(kelvin_convert(n['main']['temp']), 1), kelvin_convert(n['main']['feels_like']), n['weather'][0]['description'], n['wind']['speed']]
  #   weather.append(day)
  # return weather, city

