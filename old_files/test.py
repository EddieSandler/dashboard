import yahooquery as yq
from yahooquery import Ticker,Screener
import pandas as pd
from fredapi import Fred


# this section gets Key  US Economic indicators sourced by  FRED API

fred = Fred(api_key='d22bd9f76f161e719911783b0b7d8bfd')

gdp = list(fred.get_series('GDP'))
gnp = list(fred.get_series('GNPCA'))
cpi=list(fred.get_series('CPIAUCSL'))
unemp=list(fred.get_series('UNRATE'))
mort=list(fred.get_series('MORTGAGE30US'))
prod=list(fred.get_series('INDPRO'))
pr=list(fred.get_series('PAYEMS'))
claims=(fred.get_series('ICSA'))
fed=(fred.get_series('FEDFUNDS'))



#This section displays the key Economic Indicators
print('Economic Data')
print('GDP',gdp[-1])
print('GNP',gnp[-1])
print('CPI',cpi[-1])
print('Unemployment',unemp[-1])
print('Initial Claims',claims.iloc[-1])
print('30 yr Mortgage',mort[-1])
print('FED FUNDS',fed.iloc[-1])
print('Industrial Production',prod[-1])
print('NON FARM PR',pr[-1])

print('====================')


# this section displays current quote data for a ticker
# quote='btc-usd'
# btc= Ticker(quote)
# print(btc.price)



# print('Quote Summary')
# print(my_quote.summary_detail)

# print(aapl.summary_detail)





# regular_market_price = tickers.quotes['TSLA']['regularMarketPrice']
# regular_market_price_change = tickers.quotes['TSLA']['regularMarketChangePercent']
# print(tickers.quotes['TSLA']['displayName'], regular_market_price,regular_market_price_change)

# print('===========================')
# print('Market Summary')

# data=yq.get_market_summary(country='united states')
# for item in data:
#     try:
#         print(item['longName'],item['regularMarketPrice']['fmt'],item['regularMarketChangePercent']['fmt'])

#     except KeyError:
#         print(item['shortName'],item['regularMarketPrice']['fmt'],item['regularMarketChangePercent']['fmt'])
# print('==================================')
# print('COMPANY NEWS')
# news_count=5
# company_news= yq.search(tickers, news_count={news_count})
# for story in range(news_count):
#     print(company_news['news'][story]['title'])
#     print(company_news['news'][story]['link'])

# print('============================')
# print('US NEWS HEADLINES')
# us_news= yq.search('https://news.yahoo.com/us',news_count=5)

# for i in range(len(us_news['news'])):
#     print(us_news['news'][i]['title'])
#     print(us_news['news'][i]['link'])

# s=Screener()
#data = s.get_screeners('most_actives', count=10)
# print('TODAY"S MOST ACTIVE STOCKS')
##for item in data['most_actives']['quotes']:

#print(item['symbol'],item['regularMarketPrice'],item['regularMarketChange'],item['longName'])
# print('print tickers')
# tickers = Ticker(['aapl', 'msft'])
# prices = tickers.price
# print(prices)


# for key,value in prices.items():
#     print(key,value['regularMarketPrice'],value['regularMarketChangePercent'],value['longName'])



# Create a Ticker object
# ticker = Ticker('^GSPC')

# Fetch news for the ticker


# Print the raw news data to inspect its structure

# ticker = Ticker('aapl')

# try:
#     news = ticker.news()
#     if 'error' in news:
#         print("Error fetching news:", news)
#     else:
#         for article in news:
#             print(article['title'])
#             print(article['url'])
# except Exception as e:
#     print("An error occurred:", e)



aapl = Ticker('aapl')

# Fetch news for the ticker
mynews = aapl.news()
print(mynews)

# # Iterate through the news items and print the headlines
# for article in news:
#     print(article['title'])
#     print(article['link'])  # Link to the full article
#     print()  # Print a