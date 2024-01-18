import yahooquery as yq

from fredapi import Fred
import requests
import openai
from openai import OpenAI
from urllib.parse import quote
from flask_cors import CORS
from flask import Flask, request, render_template, jsonify,redirect, flash, session
from secret import OPENAI_API_KEY,FRED_API_KEY,JOKE_API_KEY,WEATHER_API_KEY

import datetime

today = datetime.date.today()
end = today + datetime.timedelta(days=10)



fred = Fred(api_key=FRED_API_KEY)
client = OpenAI()


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def show_dashboard():
    return render_template('portfolio.html')

@app.route('/market_summary')
def get_market_summary():
    data=yq.get_market_summary(country='united states')
    # for item in data:
    #     try:
    #         print(item['longName'],item['regularMarketPrice']['fmt'],item['regularMarketChangePercent']['fmt'])

    #     except KeyError:
    #         print(item['shortName'],item['regularMarketPrice']['fmt'],item['regularMarketChangePercent']['fmt'])
    return render_template('market_summary.html',data=data)

# @app.route('/quote',methods=['GET','POST'])
# def get_quote():
#     symbol = request.form['ticker'].upper()
#     quote = yq.Ticker(symbol)
#     data=quote.quotes[symbol]
    # name=quote.quotes[symbol]['shortName']
    # price = quote.quotes[symbol]['regularMarketPrice']
    # change = quote.quotes[symbol]['regularMarketChangePercent']
    # range=quote.quotes[symbol]['regularMarketDayRange']
    # open=quote.quotes[symbol]['regularMarketOpen']
    # prev_close=quote.quotes[symbol]['regularMarketPreviousClose']
    # bid_size=quote.quotes[symbol]['bid']
    # ask=quote.quotes[symbol]['ask']
    # bid_size=quote.quotes[symbol]['bidSize']
    # ask_size=quote.quotes[symbol]['askSize']
    # company_news=get_company_news(symbol)
    # return render_template('quote.html',data=data,news=company_news,symbol=symbol)

@app.route('/economic_data')
def show_economic_data():

    economic_indicators={
        'GDP:':'GDP',
        'GNP:':'GNPCA',
        'CPI:':'CPIAUCSL',
        'Unemployment:':'UNRATE',
        '30-Yr Mortgage:':'MORTGAGE30US',
        'FED FUNDS:':'FEDFUNDS',
        'Industrial Production:':'INDPRO',
        'Non FArm Payrolls:':'PAYEMS',
        'Initial Jobless Claims:':'ICSA'

        }
    data = {key: get_eco_data(value) for key, value in economic_indicators.items()}
    return render_template('economic_data.html', data=data)

def get_eco_data(ticker):

    response=fred.get_series(ticker)
    return response

@app.route('/calendar')
def get_eco_calendar():
    url= f'https://api.stlouisfed.org/fred/releases/dates?realtime_start={today}&realtime_end={end}&limit=10&file_type=json&api_key={FRED_API_KEY}'
    response = requests.get(url)
    data = response.json()

    return render_template('economic_calendar.html',data=data)




@app.route('/us_news')
def get_us_news():
    us_news= yq.search('https://news.yahoo.com/us',news_count=5)

    return render_template('us_news.html',news=us_news)




def get_company_news(symbol):

    news_count=5
    news= yq.search(symbol, news_count={news_count})

    return news




@app.route('/horoscope')
def test_gpt(sign='gemini'):
    openai.api_key = OPENAI_API_KEY

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"retrieve the  Daily Horoscope for  {sign}  ."},
            {"role": "user", "content": f"display a 3 line summary of the horoscope."}

        ]
    )
    msg = completion.choices[0].message
    return render_template('horoscope.html', msg=msg)

@app.route('/joke')
def joke_of_the_day():
    joke_url = "https://world-of-jokes1.p.rapidapi.com/v1/jokes/random-joke-by-category"
    querystring = {"category":"Deep Thoughts"}
    headers = {
    "X-RapidAPI-Key": f"{JOKE_API_KEY}",
    "X-RapidAPI-Host": "world-of-jokes1.p.rapidapi.com"
}
    response = requests.get(joke_url, headers=headers, params=querystring)

    joke=response.json()

    return render_template('joke.html',joke=joke['body'])

@app.route('/weather')
def get_weather():
    base_url = "https://open-weather13.p.rapidapi.com/city/"
    city ="Miami Beach"
    encoded_city=quote(city)


    headers = {"X-RapidAPI-Key":f"{WEATHER_API_KEY}",
               "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"}

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

    return render_template('weather.html',temp=current_temp)

@app.route('/quote/<symbol>')
def get_quote(symbol):
    quote = yq.Ticker(symbol)
    data = quote.quotes[symbol]
    return jsonify(data)  # Convert to JSON response


@app.route('/update_watchlist',methods=['POST'])
def update_watchlist():
    data = request.json

    tickers = yq.Ticker(data)
    prices = tickers.price
    print(jsonify(prices))
    return prices





# from flask import Flask, request, render_template, redirecYour application running on port 5000 is available. Set, flash, session
# import requests
# from secret import API_KEY

# app = Flask(__name__)
# app.app_context().push()
# app.config['SECRET_KEY'] = "never-tell!"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


# #alphavantage
# BASE_URL='https://www.alphavantage.co/query?'

# function='GLOBAL_QUOTE'
# # symbol='AAPL'

# https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey=API_KEY


# @app.route('/')
# def enter_ticker():
#     return render_template('input_ticker.html')

# @app.route('/data',methods=['GET','POST'])
# def equities():
#     ticker = request.form['ticker']

#     quote_data = get_quotes(ticker)

#     news=get_news(ticker)

#     return render_template('quote.html',quote=quote_data,news=news)


# def get_quotes(ticker):
#     url=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"

#     r = requests.get(url)
#     data= r.json()





#     return data

# def get_news(ticker):
#     url=f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={API_KEY}"


#     r = requests.get(url)
#     headlines = r.json()

#     return headlines
# # https://api.stockdata.org/v1/news/all?symbols=TSLA,AMZN,MSFT&filter_entities=true&language=en&api_token=Zrm3ez7JBHiM7mfGmuJlccTh8FCDQLljyD1QYI43


#     # # Access specific elements
#     # symbol = global_quote["01. symbol"]
#     # price = global_quote["05. price"]
#     # high=global_quote["03. high"]
#     # low=global_quote["04. low"]
#     # previous=global_quote["08. previous close"]
#     # change=global_quote["09. change"]
#     # pct_change=global_quote["10. change percent"]

#     # print("Symbol:", symbol)
#     # print("Price:", price)
#     # print("change:", change)
#     # print("Pct", pct_change)

