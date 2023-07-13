from config import *
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")

def coords():
  data = json.load(urlopen("http://ipinfo.io/json"))
  return str(data['city'])
