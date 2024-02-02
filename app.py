import yahooquery as yq
from fredapi import Fred
import requests
import openai
from openai import OpenAI
from urllib.parse import quote
from flask_cors import CORS
from flask import Flask, request, render_template, jsonify,redirect, url_for,flash, session
from secret import OPENAI_API_KEY,FRED_API_KEY,WEATHER_API_KEY
from models import db, User,Watchlist # Import the models
from forms import RegisterForm,LoginForm # Import the form
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError





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


'''===========LOGIN and AUTHENTICATION=============='''


@app.route("/")
def homepage():
    """Show homepage with links to site areas."""

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user: produce form & handle form submission."""

    form = RegisterForm()

    if  form.is_submitted() and form.validate() :
        name = form.username.data
        pwd = form.password.data

        try:
            user = User.register(name, pwd)
            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id
            return redirect("/dashboard")
        except Exception:
            db.session.rollback()  # Important to roll back the session
            flash('That username is already taken. Please choose a different one.')
            return redirect('/')
    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Produce login form or handle login."""

    form = LoginForm()

    if  form.is_submitted() and form.validate() :
        name = form.username.data
        pwd = form.password.data

        # authenticate will return a user or False
        user = User.authenticate(name, pwd)

        if user:
            session["user_id"] = user.id  # keep logged in
            return render_template('dashboard.html',id=user.id)

        else:
            form.username.errors = ["Bad name/password"]

    return render_template("login.html", form=form)
# end-login


@app.route("/dashboard")
def dashboard():
    """Example hidden page for logged-in users only."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

        # alternatively, can return HTTP Unauthorized status:
        #
        # from werkzeug.exceptions import Unauthorized
        # raise Unauthorized()

    else:
        return render_template("dashboard.html")


@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")

    return redirect("/")
'''=========================================================='''
'''====================== QUOTES AND WATCHLIST==============='''


@app.route('/quote/<symbol>')
def get_quote(symbol):
    quote = yq.Ticker(symbol)
    data = quote.quotes[symbol]
    return jsonify(data)  # Convert to JSON response



@app.route('/add_ticker',methods=['POST'])
def add_ticker_to_db():
    data = request.get_json()
    existing_entry = Watchlist.query.filter_by(ticker_code=data['ticker_code'], user_id=data['user_id']).first()
    if existing_entry:
        return "This ticker code already exists for the user.", 400

        new_entry = Watchlist(
            ticker_code=data['ticker_code'],
            ticker_name=data['ticker_name'],
            ticker_type=data['ticker_type'],
            user_id=data['user_id']
        )

        db.session.add(new_entry)
        db.session.commit()
        return 'Entries added to watchlist', 200

  















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









@app.route('/delete_ticker/<ticker>', methods=['POST'])
def delete_ticker_from_db(ticker):



    # Find the ticker by id
    ticker_to_delete = Watchlist.query.filter_by(ticker_code=ticker).first()


    if ticker_to_delete:
        # Delete the ticker from the database
        db.session.delete(ticker_to_delete)
        db.session.commit()
        return jsonify({'message': 'Ticker deleted successfully'}), 200
    else:
        return jsonify({'error': 'Ticker not found'}), 404



@app.route('/get_watchlist/<id>')
def retrieve_watchlist(id):

    ticker_codes = Watchlist.query.filter(Watchlist.user_id == id).with_entities(Watchlist.ticker_code).all()
    ticker_code_list = [ticker_code[0] for ticker_code in ticker_codes]
    response=jsonify(ticker_code_list)

    print('here is the list ',response)




    return response





@app.route('/update_watchlist/',methods=['POST'])
def update_watchlist():
    data = request.json
    ticker_list=data['watchlist']






    tickers = yq.Ticker(ticker_list)
    prices = tickers.price

    return prices
