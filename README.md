# Capstone Project One

[Deployment URL:](https://us-econ-dashboard.onrender.com/)

## Summary

This project is a dashboard intended to provide a snapshot of US Markets. It is my take on a typical Yahoo Finance screen, providing quotes for equities, currencies (including crypto), fixed income, and commodities.

## Technologies Used

The technologies utilized in this project include:

- **Front End**: JavaScript
- **Back End**: Python/Flask
- **API Calls**: Axios
- **Forms & Database**: Flask-WTF forms, SQLAlchemy/Postgres
- **Security**: Bcrypt for login/hashing
- **Libraries**: Multiple APIs and several Python 3rd party libraries

## Dashboard Components

### Quotes/ Watchlist

- **Functionality**: Provides quote data sourced by the YahooQuery library for Python.
- **Updates**: Prices updated every 20 seconds.
- **Features**: Users can add a ticker to a watchlist, stored in the database and reloaded upon login.

### Market Summary

- **Description**: A set of market data covering all US Markets.
- **Source**: Sourced through YahooQuery and updated periodically.

### News

- **Content**: Top US news headlines from Yahoo, provided by YahooQuery.

### Key Economic Indicators/Economic Data Release

- **Source**: Sourced by the St Louis Federal Reserve and accessed via the FRED API for Python.
- **Details**: Data remains static until updated by the Fed. Release data includes the current day's scheduled data release, with links to their press release.

### Additional Features

#### Horoscope

- **Source**: Utilizing the OpenAI API.
- **Offerings**: Daily horoscopes provided for the selected sign.

#### Weather

- **Source**: Sourced by the Tomorrow.io API.
- **Details**: Weather conditions for any city are provided.

#### Jokes on Demand

- **Source**: Accessed via the ICanHazDadJoke API.
- **Purpose**: To provide a quick chuckle.
