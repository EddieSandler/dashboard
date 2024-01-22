import yahooquery as yq
from fredapi import Fred
import requests
import openai
from openai import OpenAI
from urllib.parse import quote
from flask_cors import CORS
from flask import Flask, request, render_template, jsonify,redirect, url_for,flash, session
from secret import OPENAI_API_KEY,FRED_API_KEY,JOKE_API_KEY,WEATHER_API_KEY
from models import db, User, Watchlist # Import the models
from forms import UserForm # Import the form
import datetime
from flask_sqlalchemy import SQLAlchemy





today = datetime.date.today()
end = today + datetime.timedelta(days=10)



fred = Fred(api_key=FRED_API_KEY)
client = OpenAI()


app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///econ_dashboard'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)
app.app_context().push()



db.create_all()




@app.route('/')
def show_login():
    return redirect('/register')

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
def test_gpt(sign='gemini'):#change to form input for horoscope
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
    city ="Miami Beach"#change to form input for city
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

@app.route('/register',methods=['GET','POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            login_id=form.login_id.data,
            horoscope_sign=form.horoscope_sign.data,
            city=form.city.data
        )
        db.session.add(new_user)
        db.session.commit()
        print("New User:", new_user)
        print("New User ID:", new_user.id)

        # Assuming new_user now has a 'user_id' attribute after being committed
        return render_template('portfolio.html', userId=new_user.id)

    return render_template('login.html', form=form)


@app.route('/send_ticker',methods=['GET','POST'])
def add_ticker_to_db():
    data = request.get_json()
    new_entry = Watchlist(
            ticker_code=data['ticker_code'],
            ticker_name=data['ticker_name'],
            ticker_type=data['ticker_type'],
            user_id=data['user_id']
        )
    db.session.add(new_entry)

    db.session.commit()
    # db.session.add(new_entry)

    # db.session.commit()
    return 'Entries added to watchlist', 200
    # watchList=  Watchlist(
    #     ticker_code =data['ticker'],
    #     ticker_name = data['ticker_name'],
    #     ticker_type = data['ticker_type'],
    #     user_id= data['user_id']
    # )





    # print('here is new dict',new_dict)
    # watchlist=Watchlist(**new_dict)
    # db.session.add(watchList)
    # db.session.commit()

# Add to the session and commit




    # print(data.keys())
    # print(data.values())

    # print(data['ticker_type'])
    # print(data['ticker_name'])
    # print(data['user_id'])

    # print(f"ticker_code = add {data['ticker_code']} to the db")
    # print(f"ticker name = add {data['ticker_name']} to the db")
    # # print(f"ticker type =add {data['ticker_type']} to the db")
    # print(f"user id = add {data['user_id']} to the db")


    #     data['ticker_code']=data.get('ticker_code'),
    #     ticker_name=data.get('ticker_name'),
    #     ticker_type=data.get('ticker_type'),
    #     user_id=data.get('user_id')

    # print('ticker is ',new_watchlist.ticker_code)
    # print('name is: ',new_watchlist.ticker_name)
    # print('type is: ', new_watchlist.ticker_type)
    # print('user id is : ',new_watchlist.user_id)

    # # db.session.add(new_watchlist)
    # db.session.commit()


    # jsonify({'message': 'New watchlist item added successfully!'}), 201

