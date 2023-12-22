from flask import Flask, request, render_template, redirect, flash, session
import requests

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



BASE_URL='https://www.alphavantage.co/query?'
API_KEY='SE5ZHEU9MXJIPVZM'
function='GLOBAL_QUOTE'
symbol='AAPL'


@app.route('/')
def enter_ticker():
    return render_template('input_ticker.html')

@app.route('/data',methods=['GET','POST'])
def get_quote():
    ticker = request.form['ticker']

    stock_data = call_api(ticker)
    print(f"{stock_data}")
    return f"{stock_data}"


def call_api(ticker):
    url=f"{BASE_URL}function={function}&symbol={ticker}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    global_quote = data["Global Quote"]
    return global_quote


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

