from flask import Flask, request, render_template, redirect, flash, session
import requests
from secret import API_KEY

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


#alphavantage
BASE_URL='https://www.alphavantage.co/query?'
# API_KEY='SE5ZHEU9MXJIPVZM'
function='GLOBAL_QUOTE'
# symbol='AAPL'

# #StockData
# BASE_URL='https://api.stockdata.org/v1/'
# API_TOKEN='Zrm3ez7JBHiM7mfGmuJlccTh8FCDQLljyD1QYI43'


@app.route('/')
def enter_ticker():
    return render_template('input_ticker.html')

@app.route('/data',methods=['GET','POST'])
def equities():
    ticker = request.form['ticker']

    quote_data = get_quotes(ticker)

    news=get_news(ticker)

    return render_template('quote.html',quote=quote_data,news=news)


def get_quotes(ticker):
    url=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"

    r = requests.get(url)
    data= r.json()





    return data

def get_news(ticker):
    url=f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={API_KEY}"


    r = requests.get(url)
    headlines = r.json()

    return headlines
# https://api.stockdata.org/v1/news/all?symbols=TSLA,AMZN,MSFT&filter_entities=true&language=en&api_token=Zrm3ez7JBHiM7mfGmuJlccTh8FCDQLljyD1QYI43


    # # Access specific elements
    # symbol = global_quote["01. symbol"]
    # price = global_quote["05. price"]
    # high=global_quote["03. high"]
    # low=global_quote["04. low"]
    # previous=global_quote["08. previous close"]
    # change=global_quote["09. change"]
    # pct_change=global_quote["10. change percent"]

    # print("Symbol:", symbol)
    # print("Price:", price)
    # print("change:", change)
    # print("Pct", pct_change)

