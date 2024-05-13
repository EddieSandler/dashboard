from yahooquery import Ticker

ticker = Ticker('AAPL')
latest_news = ticker.news()

print(latest_news)