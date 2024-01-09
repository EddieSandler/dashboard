import yahooquery as yq
import pandas as pd
from fredapi import Fred
import requests
import openai
from openai import OpenAI
from flask import Flask, request, render_template, redirect, flash, session
from secret import OPENAI_API_KEY,FRED_API_key,JOKE_API_KEY
fred = Fred(api_key=FRED_API_key)
client = OpenAI()
app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



@app.route('/market_summary')
def get_market_summary():
    data=yq.get_market_summary(country='united states')
    for item in data:
        try:
            print(item['longName'],item['regularMarketPrice']['fmt'],item['regularMarketChangePercent']['fmt'])

        except KeyError:
            print(item['shortName'],item['regularMarketPrice']['fmt'],item['regularMarketChangePercent']['fmt'])
    return data


@app.route('/economic_data')
def show_economic_data():

    tickers={
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
    data = {key: get_eco_data(value) for key, value in tickers.items()}
    return render_template('economic_data.html', data=data)

def get_eco_data(ticker):

    response=fred.get_series(ticker)
    return response

@app.route('/us_news')
def get_us_news():
    us_news= yq.search('https://news.yahoo.com/us',news_count=5)
    for i in range(len(us_news['news'])):
        print(us_news['news'][i]['title'])
        print(us_news['news'][i]['link'])
    return render_template('us_news.html',news=us_news)



@app.route('/company_news')
def get_company_news():
    symbol='aapl'
    # tickers= yq.Ticker(symbol)
    news_count=5
    company_news= yq.search(symbol, news_count={news_count})
    for i in range(len(company_news['news'])):
        print(company_news['news'][i]['title'])
        print(company_news['news'][i]['link'])


    return render_template('company_news.html',news=company_news)




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









# from flask import Flask, request, render_template, redirect, flash, session
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

