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
end = today + datetime.timedelta(days=5)



fred = Fred(api_key=FRED_API_KEY)
client = OpenAI()


app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///econ_dashboard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
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

    return data



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
        'Non Farm Payrolls:':'PAYEMS',
        'Initial Jobless Claims:':'ICSA'

        }
    data = {key: get_eco_data(value) for key, value in economic_indicators.items()}
    return data

def get_eco_data(ticker):

    response=fred.get_series(ticker)
    return response[-1]

@app.route('/calendar')
def get_eco_calendar():
    url= f'https://api.stlouisfed.org/fred/releases/dates?realtime_start={today}&realtime_end={end}&limit=10&file_type=json&api_key={FRED_API_KEY}'
    response = requests.get(url)
    data = response.json()
    links=[]

    for item in data['release_dates']:
        id=item['release_id']


        links.append(get_link(id))
    return links







def get_link(id):
    url=f'https://api.stlouisfed.org/fred/release?release_id={id}&api_key={FRED_API_KEY}&file_type=json'
    response = requests.get(url)
    data = response.json()
    my_dict={}


    for item in data['releases']:
        name = item['name']
        link = item.get('link', 'NA')
    if name not in my_dict:
        my_dict[name] = link
    else:
        my_dict[name]=link
    return my_dict














@app.route('/us_news')
def get_us_news():
    us_news= yq.search('https://news.yahoo.com/us',news_count=5)

    return us_news




def get_company_news(symbol):

    news_count=5
    news= yq.search(symbol, news_count={news_count})
    return news


@app.route('/horoscope/<sign>',methods=['GET'])
def test_gpt(sign):
    openai.api_key = OPENAI_API_KEY
    print(sign)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"retrieve the  Daily Horoscope for  {sign}  ."},
            {"role": "user", "content": f"display a 3 line summary of the horoscope."}

        ]
    )
    msg = completion.choices[0].message.content




    response=str(msg)

    return response


@app.route('/joke')
def joke_of_the_day():

    headers={"Accept":"application/json"}
    url="https://icanhazdadjoke.com"
    response = requests.get(url,headers=headers)


    joke=response.json()['joke']

    return joke





@app.route('/weather/<city>')
def get_weather(city):
    encoded_city=quote(city)
    base_url =f"https://api.tomorrow.io/v4/weather/realtime?location={encoded_city}&units=imperial&apikey={WEATHER_API_KEY}"




    headers = {"accept": "application/json"}

    response = requests.get(base_url, headers=headers)

    weather=response.json()
    print(response)
    # degree_symbol = '\u00B0'


    return weather



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

        print("User ID:", new_user.id)

        # Assuming new_user now has a 'user_id' attribute after being committed
        return render_template('dashboard.html', userId=new_user.id)

    return render_template('login.html', form=form)


@app.route('/add_ticker',methods=['GET','POST'])
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

    return 'Entries added to watchlist', 200


@app.route('/delete_ticker/<ticker>', methods=['POST'])
def delete_ticker_from_db(ticker):
   


    # data = request.get_json()
    # ticker = data.get('ticker_code')

    # Find the ticker by id
    ticker_to_delete = Watchlist.query.filter_by(ticker_code=ticker).first()


    if ticker_to_delete:
        # Delete the ticker from the database
        db.session.delete(ticker_to_delete)
        db.session.commit()
        return jsonify({'message': 'Ticker deleted successfully'}), 200
    else:
        return jsonify({'error': 'Ticker not found'}), 404