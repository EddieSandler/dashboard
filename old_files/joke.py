import requests
from secret import JOKE_API_KEY

joke_url = "https://world-of-jokes1.p.rapidapi.com/v1/jokes/random-joke-by-category"

querystring = {"category":"Deep Thoughts"}

headers = {
	"X-RapidAPI-Key": f"{JOKE_API_KEY}",
	"X-RapidAPI-Host": "world-of-jokes1.p.rapidapi.com"
}

response = requests.get(joke_url, headers=headers, params=querystring)

joke=response.json()

print('Deep Thought of the Day: ',joke['body'])