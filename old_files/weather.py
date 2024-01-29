import requests
from urllib.parse import quote
from secret import WEATHER_API_KEY

base_url = "https://open-weather13.p.rapidapi.com/city/"
city ="Miami Beach"
encoded_city=quote(city)


headers = {
	"X-RapidAPI-Key":f"{WEATHER_API_KEY}",
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

response = requests.get(base_url+encoded_city, headers=headers)

weather=response.json()
degree_symbol = '\u00B0'
current_temp=round(weather['main']['temp'])
high_temp= round(weather['main']['temp_max'])
low_temp=round(weather['main']['temp_min'])
humidity=round(weather['main']['humidity'])

print('Weather in ',city)
print('Current Temp: ',current_temp,degree_symbol)
print('High: ',high_temp,degree_symbol)
print('Low: ',low_temp,degree_symbol)
print('Humidity: ',humidity,'%')


