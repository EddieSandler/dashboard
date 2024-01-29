

from yahooquery import Ticker

ticker = Ticker('^DJI')
latest_news = ticker.news()




quotes={"Global Quote": { "01. symbol": "IBM",
                         "02. open": "161.2900","03. high": "161.8000",
                         "04. low": "160.0100","05. price": "160.0500",
                         "06. volume": "4865797","07. latest trading day": "2023-12-20",
                         "08. previous close": "161.5600","09. change": "-1.5100",
                         "10. change percent": "-0.9346%"}}
for key,value in quotes["Global Quote"].items():
    print(f'{key},: {value}')


GDP={
    "name": "Real Gross Domestic Product per Capita",
    "interval": "quarterly",
    "unit": "chained 2012 dollars",
    "data": [
        {
            "date": "2023-07-01",
            "value": "67036.0"
        },
        {
            "date": "2023-04-01",
            "value": "66341.0"
        },
        {
            "date": "2023-01-01",
            "value": "66078.0"
        },
        {
            "date": "2022-10-01",
            "value": "65783.0"
        }

    ]

}
print(GDP['name'])
print('=============')
for data in GDP['data']:
    print(f'{data}')




CPI={
    "name": "Consumer Price Index for all Urban Consumers",
    "interval": "monthly",
    "unit": "index 1982-1984=100",
    "data": [
        {
            "date": "2023-11-01",
            "value": "307.051"
        },
        {
            "date": "2023-10-01",
            "value": "307.671"
        },
        {
            "date": "2023-09-01",
            "value": "307.789"
        },
        {
            "date": "2023-08-01",
            "value": "307.026"
        },
        {
            "date": "2023-07-01",
            "value": "305.691"
        },
        {
            "date": "2023-06-01",
            "value": "305.109"
        },
        {
            "date": "2023-05-01",
            "value": "304.127"
        },
        {
            "date": "2023-04-01",
            "value": "303.363"
        },
        {
            "date": "2023-03-01",
            "value": "301.836"
        },
        {
            "date": "2023-02-01",
            "value": "300.840"
        }
    ]
}
print('=================')
print(CPI['name'])
for data in CPI['data']:
    print(f'{data}')



print('============')

INFLATION={
    "name": "Inflation - US Consumer Prices",
    "interval": "annual",
    "unit": "percent",
    "data": [
        {
            "date": "2022-01-01",
            "value": "8.00279982052121"
        },
        {
            "date": "2021-01-01",
            "value": "4.69785886363742"
        },
        {
            "date": "2020-01-01",
            "value": "1.23358439630629"
        },
        {
            "date": "2019-01-01",
            "value": "1.81221007526021"
        },
        {
            "date": "2018-01-01",
            "value": "2.44258329692817"
        },
        {
            "date": "2017-01-01",
            "value": "2.13011000365961"
        },
        {
            "date": "2016-01-01",
            "value": "1.26158320570536"
        },
        {
            "date": "2015-01-01",
            "value": "0.118627135552451"
        },
        {
            "date": "2014-01-01",
            "value": "1.62222297740817"
        },
        {
            "date": "2013-01-01",
            "value": "1.46483265562717"
        }
    ]
}

print(INFLATION['name'])
for data in INFLATION['data']:
    print(f'{data}')

print('=============')
RETAIL_SALES= {
    "name": "Advance Retail Sales: Retail Trade",
    "interval": "monthly",
    "unit": "millions of dollars",
    "data": [
        {
            "date": "2023-11-01",
            "value": "625140.0"
        },
        {
            "date": "2023-10-01",
            "value": "607013.0"
        },
        {
            "date": "2023-09-01",
            "value": "593695.0"
        },
        {
            "date": "2023-08-01",
            "value": "628192.0"
        },
        {
            "date": "2023-07-01",
            "value": "605403.0"
        },
        {
            "date": "2023-06-01",
            "value": "612243.0"
        },
        {
            "date": "2023-05-01",
            "value": "631496.0"
        },
        {
            "date": "2023-04-01",
            "value": "588220.0"
        },
        {
            "date": "2023-03-01",
            "value": "604084.0"
        },
        {
            "date": "2023-02-01",
            "value": "529374"
        },
        {
            "date": "2023-01-01",
            "value": "547156"
        },
        {
            "date": "2022-12-01",
            "value": "654825"
        },
        {
            "date": "2022-11-01",
            "value": "605205"
        },
        {
            "date": "2022-10-01",
            "value": "597170"
        },
        {
            "date": "2022-09-01",
            "value": "577966"
        }
    ]
}
print(RETAIL_SALES["name"])
print(f'interval:{RETAIL_SALES["interval"]}')
print(f'unit: {RETAIL_SALES["unit"]}')


for data in RETAIL_SALES['data']:
    print(f'{data}')

print('=============')

DURABLE_GOODS={
    "name": "Manufacturer New Orders: Durable Goods",
    "interval": "monthly",
    "unit": "millions of dollars",
    "data": [
        {
            "date": "2023-11-01",
            "value": "286625.0"
        },
        {
            "date": "2023-10-01",
            "value": "278909.0"
        },
        {
            "date": "2023-09-01",
            "value": "308103.0"
        },
        {
            "date": "2023-08-01",
            "value": "290578.0"
        },
        {
            "date": "2023-07-01",
            "value": "261612.0"
        },
        {
            "date": "2023-06-01",
            "value": "324238.0"
        },
        {
            "date": "2023-05-01",
            "value": "288640.0"
        },
        {
            "date": "2023-04-01",
            "value": "272375"
        },
        {
            "date": "2023-03-01",
            "value": "312535"
        },
        {
            "date": "2023-02-01",
            "value": "256827"
        },
        {
            "date": "2023-01-01",
            "value": "254810"
        }
    ]
}

print(DURABLE_GOODS["name"])
print(f'interval:{DURABLE_GOODS["interval"]}')
print(f'unit: {DURABLE_GOODS["unit"]}')


for data in DURABLE_GOODS['data']:
    print(f'{data}')

print('=============')

UNEMPLOYMENT= {
    "name": "Unemployment Rate",
    "interval": "monthly",
    "unit": "percent",
    "data": [
        {
            "date": "2023-11-01",
            "value": "3.7"
        },
        {
            "date": "2023-10-01",
            "value": "3.9"
        },
        {
            "date": "2023-09-01",
            "value": "3.8"
        },
        {
            "date": "2023-08-01",
            "value": "3.8"
        },
        {
            "date": "2023-07-01",
            "value": "3.5"
        },
        {
            "date": "2023-06-01",
            "value": "3.6"
        },
        {
            "date": "2023-05-01",
            "value": "3.7"
        },
        {
            "date": "2023-04-01",
            "value": "3.4"
        },
        {
            "date": "2023-03-01",
            "value": "3.5"
        },
        {
            "date": "2023-02-01",
            "value": "3.6"
        },
        {
            "date": "2023-01-01",
            "value": "3.4"
        },
        {
            "date": "2022-12-01",
            "value": "3.5"
        },
        {
            "date": "2022-11-01",
            "value": "3.6"
        },
        {
            "date": "2022-10-01",
            "value": "3.7"
        },
        {
            "date": "2022-09-01",
            "value": "3.5"
        },
        {
            "date": "2022-08-01",
            "value": "3.7"
        },
        {
            "date": "2022-07-01",
            "value": "3.5"
        },
        {
            "date": "2022-06-01",
            "value": "3.6"
        },
        {
            "date": "2022-05-01",
            "value": "3.6"
        },
        {
            "date": "2022-04-01",
            "value": "3.6"
        },
        {
            "date": "2022-03-01",
            "value": "3.6"
        },
        {
            "date": "2022-02-01",
            "value": "3.8"
        },
        {
            "date": "2022-01-01",
            "value": "4.0"
        },
        {
            "date": "2021-12-01",
            "value": "3.9"
        },
        {
            "date": "2021-11-01",
            "value": "4.2"
        },
        {
            "date": "2021-10-01",
            "value": "4.5"
        },
        {
            "date": "2021-09-01",
            "value": "4.8"
        },
        {
            "date": "2021-08-01",
            "value": "5.2"
        },
        {
            "date": "2021-07-01",
            "value": "5.4"
        },
        {
            "date": "2021-06-01",
            "value": "5.9"
        }
    ]
}

print(UNEMPLOYMENT["name"])
print(f'interval:{UNEMPLOYMENT["interval"]}')
print(f'unit: {UNEMPLOYMENT["unit"]}')


for data in UNEMPLOYMENT['data']:
    print(f'{data}')

print('=============')


NONFARM_PAYROLL= {
    "name": "Total Nonfarm Payroll",
    "interval": "monthly",
    "unit": "thousands of persons",
    "data": [
        {
            "date": "2023-11-01",
            "value": "158461"
        },
        {
            "date": "2023-10-01",
            "value": "157984"
        },
        {
            "date": "2023-09-01",
            "value": "156906"
        },
        {
            "date": "2023-08-01",
            "value": "156392"
        },
        {
            "date": "2023-07-01",
            "value": "156022"
        },
        {
            "date": "2023-06-01",
            "value": "156905"
        },
        {
            "date": "2023-05-01",
            "value": "156279"
        },
        {
            "date": "2023-04-01",
            "value": "155369"
        },
        {
            "date": "2023-03-01",
            "value": "154440"
        },
        {
            "date": "2023-02-01",
            "value": "153983"
        },
        {
            "date": "2023-01-01",
            "value": "152839"
        },
        {
            "date": "2022-12-01",
            "value": "155344"
        },
        {
            "date": "2022-11-01",
            "value": "155642"
        },
        {
            "date": "2022-10-01",
            "value": "155041"
        },
        {
            "date": "2022-09-01",
            "value": "153809"
        },
        {
            "date": "2022-08-01",
            "value": "153285"
        },
        {
            "date": "2022-07-01",
            "value": "152875"
        },
        {
            "date": "2022-06-01",
            "value": "153217"
        },
        {
            "date": "2022-05-01",
            "value": "152291"
        },
        {
            "date": "2022-04-01",
            "value": "151449"
        },
        {
            "date": "2022-03-01",
            "value": "150411"
        },
        {
            "date": "2022-02-01",
            "value": "149606"
        }
    ]
}

print(NONFARM_PAYROLL["name"])
print(f'interval:{NONFARM_PAYROLL["interval"]}')
print(f'unit: {NONFARM_PAYROLL["unit"]}')


for data in NONFARM_PAYROLL['data']:
    print(f'{data}')

print('===============')

NEWS={
    "items": "50",
    "sentiment_score_definition": "x <= -0.35: Bearish; -0.35 < x <= -0.15: Somewhat-Bearish; -0.15 < x < 0.15: Neutral; 0.15 <= x < 0.35: Somewhat_Bullish; x >= 0.35: Bullish",
    "relevance_score_definition": "0 < x <= 1, with a higher score indicating higher relevance.",
    "feed": [
        {
            "title": "5 Biggest Winners, 5 Biggest Losers From Dow Jones Industrial Average In 2023 - Apple  ( NASDAQ:AAPL ) , Amazon.com  ( NASDAQ:AMZN ) ",
            "url": "https://www.benzinga.com/news/24/01/36455419/5-biggest-winners-5-biggest-losers-from-dow-jones-industrial-average-in-2023",
            "time_published": "20240102T170245",
            "authors": [
                "Chris Katje"
            ],
            "summary": "Broad stock market indexes were up in 2023 with technology stocks outperforming several other sectors. Here's a look at the biggest gainers and laggards in the Dow Jones Industrial Average.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2024/Winner-Losers-Shutterstock.jpeg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "News",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999174"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Energy & Transportation",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.25"
                }
            ],
            "overall_sentiment_score": 0.180135,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.278222",
                    "ticker_sentiment_score": "0.229511",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "GOOG",
                    "relevance_score": "0.070935",
                    "ticker_sentiment_score": "0.117654",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "META",
                    "relevance_score": "0.14131",
                    "ticker_sentiment_score": "0.143607",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.210579",
                    "ticker_sentiment_score": "0.218241",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.278222",
                    "ticker_sentiment_score": "0.229511",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.14131",
                    "ticker_sentiment_score": "0.143607",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "CVX",
                    "relevance_score": "0.070935",
                    "ticker_sentiment_score": "-0.010433",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "INTC",
                    "relevance_score": "0.14131",
                    "ticker_sentiment_score": "0.23859",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AXP",
                    "relevance_score": "0.14131",
                    "ticker_sentiment_score": "0.243512",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "BA",
                    "relevance_score": "0.070935",
                    "ticker_sentiment_score": "0.199437",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Competitor Analysis: Evaluating Apple And Competitors In Technology Hardware, Storage & Peripherals Industry - Apple  ( NASDAQ:AAPL ) ",
            "url": "https://www.benzinga.com/news/24/01/36454259/competitor-analysis-evaluating-apple-and-competitors-in-technology-hardware-storage-amp-peripherals",
            "time_published": "20240102T160013",
            "authors": [
                "Benzinga Insights"
            ],
            "summary": "In today's rapidly changing and highly competitive business world, it is imperative for investors and industry observers to carefully assess companies before making investment choices.",
            "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png",
            "source": "Benzinga",
            "category_within_source": "Trading",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Earnings",
                    "relevance_score": "0.875462"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.5855"
                }
            ],
            "overall_sentiment_score": 0.24126,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.472338",
                    "ticker_sentiment_score": "0.287276",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Stock Market Done Celebrating New Year; Apple Stock Falls On Downgrade",
            "url": "https://www.investors.com/market-trend/stock-market-today/stock-market-done-celebrating-new-year-apple-stock-falls-on-downgrade/",
            "time_published": "20240102T155400",
            "authors": [
                "Investor's Business Daily",
                "KIMBERLEY KOENIG"
            ],
            "summary": "Stock Market Done Celebrating New Year. Apple Stock Falls On Downgrade Investor's Business Daily ...",
            "banner_image": "https://www.investors.com/wp-content/uploads/2023/10/Stock-Apple-shanghaistore-02-company.jpg",
            "source": "Investors Business Daily",
            "category_within_source": "n/a",
            "source_domain": "www.investors.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Blockchain",
                    "relevance_score": "0.310843"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Real Estate & Construction",
                    "relevance_score": "0.25"
                }
            ],
            "overall_sentiment_score": 0.064544,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "MARA",
                    "relevance_score": "0.118647",
                    "ticker_sentiment_score": "0.209372",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "MSTR",
                    "relevance_score": "0.234684",
                    "ticker_sentiment_score": "0.096359",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.345674",
                    "ticker_sentiment_score": "-0.162488",
                    "ticker_sentiment_label": "Somewhat-Bearish"
                },
                {
                    "ticker": "BCS",
                    "relevance_score": "0.059488",
                    "ticker_sentiment_score": "-0.108",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.290952",
                    "ticker_sentiment_score": "0.011067",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "IVZ",
                    "relevance_score": "0.059488",
                    "ticker_sentiment_score": "0.013111",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "COIN",
                    "relevance_score": "0.17715",
                    "ticker_sentiment_score": "0.212157",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "CRYPTO:BTC",
                    "relevance_score": "0.234684",
                    "ticker_sentiment_score": "0.226893",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Stocks: The Bull Market Picture Becomes More Blurry",
            "url": "https://www.investorideas.com/news/2024/main/01023TradingAlert-Stocks.asp",
            "time_published": "20240102T154143",
            "authors": [],
            "summary": "January 2, 2024 ( Investorideas.com Newswire ) On Friday, the S&P 500 index retreated from its Thursday's local high of 4,793.30. However, by the end of the day, it rebounded from the daily low of around 4,752 and closed just 0.28% lower.",
            "banner_image": None,
            "source": "Investor Ideas",
            "category_within_source": "n/a",
            "source_domain": "www.investorideas.com",
            "topics": [
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.451494"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999993"
                }
            ],
            "overall_sentiment_score": 0.029236,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.104228",
                    "ticker_sentiment_score": "0.14659",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "FOREX:USD",
                    "relevance_score": "0.052226",
                    "ticker_sentiment_score": "-0.027006",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Why Is Apple Stock Sliding Tuesday? - Apple  ( NASDAQ:AAPL ) ",
            "url": "https://www.benzinga.com/news/24/01/36453039/why-is-apple-stock-sliding-tuesday",
            "time_published": "20240102T154032",
            "authors": [
                "Anusuya Lahiri"
            ],
            "summary": "Apple Inc AAPL stock is trading lower Tuesday after Barclays analyst Tim Long downgraded the stock from Equal-Weight to Underweight and lowered the price target from $161 to $160. The analyst slightly lowered his AAPL estimates following another round of checks.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2024/01/02/iphone-15.png?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "Trading",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.214378"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.365926"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": -0.181017,
            "overall_sentiment_label": "Somewhat-Bearish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.490323",
                    "ticker_sentiment_score": "-0.362103",
                    "ticker_sentiment_label": "Bearish"
                },
                {
                    "ticker": "BCS",
                    "relevance_score": "0.130926",
                    "ticker_sentiment_score": "-0.147505",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Opportunities Ahead - Avoid Classic New Year Mistake, China And Iran Threats, Bitcoin Rumor - Tesla  ( NASDAQ:TSLA ) ",
            "url": "https://www.benzinga.com/markets/24/01/36453682/opportunities-ahead-avoid-classic-new-year-mistake-china-and-iran-threats-bitcoin-rumor",
            "time_published": "20240102T153636",
            "authors": [
                "The Arora Report"
            ],
            "summary": "To gain an edge, this is what you need to know today. Please click here for a chart of SPDR S&P 500 ETF Trust SPY which represents the benchmark stock market index S&P 500 ( SPX ) . 2024 year end targets from Wall Street strategists Sector recommendations from Wall Street strategists",
            "banner_image": "https://cdn.benzinga.com/files/wance-paleri--5vn1iu3cdk-unsplash_6.jpg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "Trading",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.204043,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.089629",
                    "ticker_sentiment_score": "-0.144205",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "GOOG",
                    "relevance_score": "0.089629",
                    "ticker_sentiment_score": "-0.144205",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "META",
                    "relevance_score": "0.089629",
                    "ticker_sentiment_score": "-0.144205",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.089629",
                    "ticker_sentiment_score": "-0.144205",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.089629",
                    "ticker_sentiment_score": "-0.144205",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.089629",
                    "ticker_sentiment_score": "0.276183",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "IVZ",
                    "relevance_score": "0.044885",
                    "ticker_sentiment_score": "0.099008",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "CRYPTO:BTC",
                    "relevance_score": "0.17813",
                    "ticker_sentiment_score": "-0.039928",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Warren Buffett's Biggest Bets in 2024: 57.4% of Berkshire Hathaway's $367.5 Billion Stock Portfolio Is Held in Just 2 Stocks",
            "url": "https://www.fool.com/investing/2024/01/02/warren-buffett-big-bet-2024-berkshire-stock-aapl/",
            "time_published": "20240102T152416",
            "authors": [
                "CFA",
                "Keith Noonan and Parkev Tatevosian"
            ],
            "summary": "Buffett has incredible confidence in these two stocks heading into 2024.",
            "banner_image": "https://media.ycharts.com/charts/acb4e0c58288d9a2fb72ace06b451678.png",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.495866"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.292142,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "BAC",
                    "relevance_score": "0.239541",
                    "ticker_sentiment_score": "0.201304",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.497609",
                    "ticker_sentiment_score": "0.415416",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "BRK-A",
                    "relevance_score": "0.048621",
                    "ticker_sentiment_score": "0.30226",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Behind Al Gore's $19 Billion Investment Firm and How He Made Millions in Apple Stock",
            "url": "https://www.fool.com/investing/2024/01/02/behind-al-gores-19-billion-investment-firm-and-how/",
            "time_published": "20240102T151645",
            "authors": [
                "Travis Hoium"
            ],
            "summary": "Is Al Gore one of the best investors of the century? He should be in the conversation.",
            "banner_image": "https://g.foolcdn.com/editorial/images/759474/blue-arrows-pointing-up-dividends-interest-rates.jpg",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.161647"
                }
            ],
            "overall_sentiment_score": 0.364341,
            "overall_sentiment_label": "Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.760593",
                    "ticker_sentiment_score": "0.699722",
                    "ticker_sentiment_label": "Bullish"
                }
            ]
        },
        {
            "title": "Market Clubhouse Morning Memo - January 2nd, 2024  ( Trade Strategy For SPY, QQQ, AAPL, MSFT, TSLA, GOOGL, META, And NVDA )  - Invesco QQQ Trust, Series 1  ( NASDAQ:QQQ ) ",
            "url": "https://www.benzinga.com/markets/24/01/36453252/market-clubhouse-morning-memo-january-2nd-2024-trade-strategy-for-spy-qqq-aapl-msft-tsla-googl-meta",
            "time_published": "20240102T151537",
            "authors": [
                "RIPS"
            ],
            "summary": "Good Morning Traders! In today's Market Clubhouse Morning Memo, we will discuss SPY, QQQ, AAPL, MSFT, TSLA, GOOGL, META, and NVDA. Our proprietary formula, exclusive to Market Clubhouse, dictates these price levels. This dynamic equation takes into account price, volume, and options flow.",
            "banner_image": "https://cdn.benzinga.com/files/market-clubhouse-morning-memo_137.png?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "Trading",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999998"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.212092,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.140896",
                    "ticker_sentiment_score": "0.155699",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "GOOG",
                    "relevance_score": "0.035397",
                    "ticker_sentiment_score": "0.076006",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.105914",
                    "ticker_sentiment_score": "0.286266",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.140896",
                    "ticker_sentiment_score": "0.028771",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.175603",
                    "ticker_sentiment_score": "0.146709",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Fidelity believes its stake in X, formerly known as Twitter, is now worth 71.5% less than when Musk bought it",
            "url": "https://www.marketwatch.com/story/fidelity-believes-its-stake-in-x-formerly-known-as-twitter-is-now-worth-71-5-less-than-when-musk-bought-it-f9076958",
            "time_published": "20240102T150000",
            "authors": [
                "Barbara Kollmeyer"
            ],
            "summary": "Fidelity has again marked down its stake in Elon Musk's social media platform, formerly known as Twitter though now called X, which the money manager helped him purchase for $44 billion.",
            "banner_image": "https://images.mktw.net/im-35185404/social",
            "source": "MarketWatch",
            "category_within_source": "Top Stories",
            "source_domain": "www.marketwatch.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": -0.133122,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "NYT",
                    "relevance_score": "0.194242",
                    "ticker_sentiment_score": "-0.296709",
                    "ticker_sentiment_label": "Somewhat-Bearish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.377142",
                    "ticker_sentiment_score": "-0.470903",
                    "ticker_sentiment_label": "Bearish"
                }
            ]
        },
        {
            "title": "Apple Downgraded, Treasury Yields Higher as Geopolitical Tensions Escalate",
            "url": "https://aap.thestreet.com/story/16141129/1/apple-downgraded-treasury-yields-higher-as-geopolitical-tensions-escalate.html",
            "time_published": "20240102T140500",
            "authors": [],
            "summary": "* An Apple downgrade, an uptick in Treasury yields, rising geopolitical tension, and oil prices have equity futures in the red for the start of 2024. * Investor sentiment remains in Extreme Greed and the market still sees six rate cuts in 2024. * This week's data may push back on rate cut ...",
            "banner_image": "http://s.thestreet.com/files/tsc/v2008/photos/contrib/uploads/53d453d1-338e-11ed-8195-497ef102cf71.jpg",
            "source": "The Street",
            "category_within_source": "GoogleRSS",
            "source_domain": "aap.thestreet.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.161647"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.310843"
                }
            ],
            "overall_sentiment_score": 0.043949,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.128135",
                    "ticker_sentiment_score": "0.120142",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.128135",
                    "ticker_sentiment_score": "0.120142",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.427597",
                    "ticker_sentiment_score": "0.166292",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "LMT",
                    "relevance_score": "0.128135",
                    "ticker_sentiment_score": "0.040333",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BCS",
                    "relevance_score": "0.064276",
                    "ticker_sentiment_score": "0.021113",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.128135",
                    "ticker_sentiment_score": "0.120142",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.128135",
                    "ticker_sentiment_score": "0.120142",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "55% of Warren Buffett's $367 Billion Portfolio Is Invested in Just 3 Stocks",
            "url": "https://www.fool.com/investing/2024/01/02/55-warren-buffetts-portfolio-invested-in-3-stocks/",
            "time_published": "20240102T133000",
            "authors": [
                "Trevor Jennewine"
            ],
            "summary": "Apple, Coca-Cola, and Visa benefit from durable competitive advantages, a quality that Warren Buffett sees as essential to a worthwhile investment.",
            "banner_image": "https://g.foolcdn.com/editorial/images/759699/investor-33.jpg",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.955357"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.999998"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.319188,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.28346",
                    "ticker_sentiment_score": "0.204655",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "KO",
                    "relevance_score": "0.249288",
                    "ticker_sentiment_score": "0.251231",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "MA",
                    "relevance_score": "0.0362",
                    "ticker_sentiment_score": "0.216844",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "V",
                    "relevance_score": "0.249288",
                    "ticker_sentiment_score": "0.276419",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "BRK-A",
                    "relevance_score": "0.0362",
                    "ticker_sentiment_score": "0.193982",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AXP",
                    "relevance_score": "0.0362",
                    "ticker_sentiment_score": "0.216844",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "PEP",
                    "relevance_score": "0.0362",
                    "ticker_sentiment_score": "0.183078",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Futures Fall As Apple Slides On Downgrade",
            "url": "https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-apple-stock-slides-on-downgrade-tesla-deliveries/",
            "time_published": "20240102T132100",
            "authors": [
                "SCOTT LEHTONEN",
                "Investor's Business Daily"
            ],
            "summary": "Dow Jones Futures Fall 200 Points As Apple Slides On Downgrade. Tesla Deliveries Imminent Investor's Business Daily ...",
            "banner_image": "https://www.investors.com/wp-content/uploads/2021/09/Stock-wallstreetflag-01-adobe.jpg",
            "source": "Investors Business Daily",
            "category_within_source": "n/a",
            "source_domain": "www.investors.com",
            "topics": [
                {
                    "topic": "Life Sciences",
                    "relevance_score": "0.2"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.2"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.2"
                },
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.2"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.2"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.158519"
                }
            ],
            "overall_sentiment_score": 0.083282,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "CALM",
                    "relevance_score": "0.077719",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NFLX",
                    "relevance_score": "0.192694",
                    "ticker_sentiment_score": "0.068294",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "CELH",
                    "relevance_score": "0.154703",
                    "ticker_sentiment_score": "0.120018",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.038906",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.116348",
                    "ticker_sentiment_score": "-0.07792",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "SNOW",
                    "relevance_score": "0.154703",
                    "ticker_sentiment_score": "0.120635",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "IVZ",
                    "relevance_score": "0.038906",
                    "ticker_sentiment_score": "0.008909",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AMGN",
                    "relevance_score": "0.154703",
                    "ticker_sentiment_score": "0.07912",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.038906",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BCS",
                    "relevance_score": "0.077719",
                    "ticker_sentiment_score": "-0.148149",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.267245",
                    "ticker_sentiment_score": "-0.023886",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "V",
                    "relevance_score": "0.154703",
                    "ticker_sentiment_score": "0.160497",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "CAT",
                    "relevance_score": "0.154703",
                    "ticker_sentiment_score": "0.211111",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "WBA",
                    "relevance_score": "0.077719",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "SPGI",
                    "relevance_score": "0.038906",
                    "ticker_sentiment_score": "-0.079072",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Apple Broke 12-Year Tradition By Skipping New iPad Release In 2023 For The First Time - Apple  ( NASDAQ:AAPL ) ",
            "url": "https://www.benzinga.com/news/24/01/36449806/apple-broke-12-year-tradition-by-skipping-new-ipad-release-in-2023-for-the-first-time",
            "time_published": "20240102T130723",
            "authors": [
                "Benzinga Neuro"
            ],
            "summary": "In an unexpected move, Apple Inc. AAPL did not unveil a new iPad model in 2023, marking the first year without an iPad release since its inception in 2010. What Happened: According to a report by MacRumors, Apple broke its 12-year tradition of annual iPad releases in 2023.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2024/Ipad-Pro-11-inch-2021-Model-With-Apple-M.jpeg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "General",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "1.0"
                }
            ],
            "overall_sentiment_score": 0.158488,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.809819",
                    "ticker_sentiment_score": "0.257614",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Apple's stock falls after 'sell' call from Barclays",
            "url": "https://www.marketwatch.com/story/apples-stock-falls-after-sell-call-from-barclays-776234de",
            "time_published": "20240102T130300",
            "authors": [
                "Tomi Kilgore"
            ],
            "summary": "Shares of Apple Inc. are starting 2024 with a selloff, after Barclays analyst Tim Long said it was \"time for a breather,\" citing weak hardware sales as iPhone 15 demand disappoints.",
            "banner_image": "https://images.mktw.net/im-08183262/social",
            "source": "MarketWatch",
            "category_within_source": "Top Stories",
            "source_domain": "www.marketwatch.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.962106"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.905476"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": -0.150932,
            "overall_sentiment_label": "Somewhat-Bearish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.369685",
                    "ticker_sentiment_score": "-0.307004",
                    "ticker_sentiment_label": "Somewhat-Bearish"
                },
                {
                    "ticker": "BCS",
                    "relevance_score": "0.127456",
                    "ticker_sentiment_score": "-0.253785",
                    "ticker_sentiment_label": "Somewhat-Bearish"
                }
            ]
        },
        {
            "title": "U.K. stock market 'in a quagmire of existential angst' as FTSE 100 celebrates 40th birthday",
            "url": "https://www.marketwatch.com/story/u-k-stock-market-in-a-quagmire-of-existential-angst-as-ftse-100-celebrates-40th-birthday-7308f041",
            "time_published": "20240102T125900",
            "authors": [
                "Jamie Chisholm"
            ],
            "summary": "London's FTSE 100 will celebrate its 40th birthday on Wednesday. But it's been a hard life for U.K's blue-chip barometer since it came of age.",
            "banner_image": "https://images.mktw.net/im-27273120?width=700&height=195",
            "source": "MarketWatch",
            "category_within_source": "Top Stories",
            "source_domain": "www.marketwatch.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999696"
                }
            ],
            "overall_sentiment_score": 0.016933,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.11983",
                    "ticker_sentiment_score": "0.011639",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.11983",
                    "ticker_sentiment_score": "0.011639",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "FOREX:GBP",
                    "relevance_score": "0.1789",
                    "ticker_sentiment_score": "0.194845",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "FOREX:EUR",
                    "relevance_score": "0.060085",
                    "ticker_sentiment_score": "-0.095",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "FOREX:USD",
                    "relevance_score": "0.060085",
                    "ticker_sentiment_score": "-0.095",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Analyst Hits Sell Button On Apple Stock As 2024 Begins. Here's Why.",
            "url": "https://www.investors.com/news/technology/apple-stock-downgraded-on-growth-concerns/",
            "time_published": "20240102T122800",
            "authors": [
                "PATRICK SEITZ",
                "Investor's Business Daily"
            ],
            "summary": "Apple Stock Downgraded On Growth Concerns Investor's Business Daily ...",
            "banner_image": "https://www.investors.com/wp-content/uploads/2023/09/Stock-Apple-chinastorefront-02-company.jpg",
            "source": "Investors Business Daily",
            "category_within_source": "n/a",
            "source_domain": "www.investors.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.929393"
                }
            ],
            "overall_sentiment_score": -0.083848,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.823417",
                    "ticker_sentiment_score": "-0.462039",
                    "ticker_sentiment_label": "Bearish"
                },
                {
                    "ticker": "BCS",
                    "relevance_score": "0.213048",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Bank of America To Rally Around 28%? Here Are 10 Top Analyst Forecasts For Tuesday - Apple  ( NASDAQ:AAPL ) , Alpha & Omega  ( NASDAQ:AOSL ) ",
            "url": "https://www.benzinga.com/news/24/01/36448915/bank-of-america-to-rally-around-28-here-are-10-top-analyst-forecasts-for-tuesday",
            "time_published": "20240102T122258",
            "authors": [
                "Avi Kapoor"
            ],
            "summary": "Top Wall Street analysts changed their outlook on these top names. For a complete view of all analyst rating changes, including upgrades and downgrades, please see our analyst ratings page. Raymond James cut Antero Resources Corporation AR price target from $37 to $28.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2024/01/02/bank_of_america_-_logo.jpg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "Trading",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Energy & Transportation",
                    "relevance_score": "0.166667"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.166667"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.166667"
                },
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.166667"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999999"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.166667"
                },
                {
                    "topic": "Real Estate & Construction",
                    "relevance_score": "0.166667"
                }
            ],
            "overall_sentiment_score": 0.111373,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "AR",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "0.118979",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "-0.117651",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BCS",
                    "relevance_score": "0.448842",
                    "ticker_sentiment_score": "-0.126364",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BAC",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "-0.056333",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "U",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "0.067599",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "WFC",
                    "relevance_score": "0.157483",
                    "ticker_sentiment_score": "0.069691",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "MS",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "-0.054272",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "EXPE",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "0.093546",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AOSL",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "0.24587",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "PK",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "0.177437",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "CMG",
                    "relevance_score": "0.234307",
                    "ticker_sentiment_score": "0.089103",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Why investors should be wary of New Year 'head fakes' that may be pointing at this asset class",
            "url": "https://www.marketwatch.com/story/why-investors-should-be-wary-of-new-year-head-fakes-that-may-be-pointing-at-this-asset-class-ba7134ad",
            "time_published": "20240102T120700",
            "authors": [
                "Barbara Kollmeyer"
            ],
            "summary": "Small-caps had a great end to 2023, but hedge funds may only be covering their shorts. Beware says our call of the day.",
            "banner_image": "https://images.mktw.net/im-59914087?width=700&height=909",
            "source": "MarketWatch",
            "category_within_source": "Top Stories",
            "source_domain": "www.marketwatch.com",
            "topics": [
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.451494"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999499"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": -0.064571,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "YY",
                    "relevance_score": "0.079921",
                    "ticker_sentiment_score": "-0.10167",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.079921",
                    "ticker_sentiment_score": "-0.158895",
                    "ticker_sentiment_label": "Somewhat-Bearish"
                },
                {
                    "ticker": "BCS",
                    "relevance_score": "0.040011",
                    "ticker_sentiment_score": "-0.152219",
                    "ticker_sentiment_label": "Somewhat-Bearish"
                },
                {
                    "ticker": "GS",
                    "relevance_score": "0.079921",
                    "ticker_sentiment_score": "-0.063678",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "JPNRF",
                    "relevance_score": "0.040011",
                    "ticker_sentiment_score": "-0.037834",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BIDU",
                    "relevance_score": "0.079921",
                    "ticker_sentiment_score": "-0.10167",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "CRYPTO:BTC",
                    "relevance_score": "0.040011",
                    "ticker_sentiment_score": "0.292073",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Is SoFi Select 500 ETF  ( SFY )  a Strong ETF Right Now?",
            "url": "https://www.zacks.com/stock/news/2204280/is-sofi-select-500-etf-sfy-a-strong-etf-right-now",
            "time_published": "20240102T112006",
            "authors": [
                "Zacks Equity Research"
            ],
            "summary": "Smart Beta ETF report for ...",
            "banner_image": "https://staticx-tuner.zacks.com/images/default_article_images/default193.jpg",
            "source": "Zacks Commentary",
            "category_within_source": "n/a",
            "source_domain": "www.zacks.com",
            "topics": [
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999483"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.27766,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.120431",
                    "ticker_sentiment_score": "0.056515",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.120431",
                    "ticker_sentiment_score": "0.056515",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "IVZ",
                    "relevance_score": "0.120431",
                    "ticker_sentiment_score": "0.143575",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.120431",
                    "ticker_sentiment_score": "0.056515",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Should Invesco Dividend Achievers ETF  ( PFM )  Be on Your Investing Radar?",
            "url": "https://www.zacks.com/stock/news/2204281/should-invesco-dividend-achievers-etf-pfm-be-on-your-investing-radar",
            "time_published": "20240102T112005",
            "authors": [
                "Zacks Equity Research"
            ],
            "summary": "Style Box ETF report for ...",
            "banner_image": "https://staticx-tuner.zacks.com/images/default_article_images/default38.jpg",
            "source": "Zacks Commentary",
            "category_within_source": "n/a",
            "source_domain": "www.zacks.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.451494"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.242505,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.123844",
                    "ticker_sentiment_score": "0.068698",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.123844",
                    "ticker_sentiment_score": "0.068698",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "IVZ",
                    "relevance_score": "0.184834",
                    "ticker_sentiment_score": "0.15868",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "UNH",
                    "relevance_score": "0.123844",
                    "ticker_sentiment_score": "0.068698",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Is FlexShares Morningstar U.S. Market Factor Tilt ETF  ( TILT )  a Strong ETF Right Now?",
            "url": "https://www.zacks.com/stock/news/2204285/is-flexshares-morningstar-us-market-factor-tilt-etf-tilt-a-strong-etf-right-now",
            "time_published": "20240102T112005",
            "authors": [
                "Zacks Equity Research"
            ],
            "summary": "Smart Beta ETF report for TILT ...",
            "banner_image": "https://staticx-tuner.zacks.com/images/default_article_images/default200.jpg",
            "source": "Zacks Commentary",
            "category_within_source": "n/a",
            "source_domain": "www.zacks.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                }
            ],
            "overall_sentiment_score": 0.204226,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.11123",
                    "ticker_sentiment_score": "0.046",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.11123",
                    "ticker_sentiment_score": "0.046",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "MORN",
                    "relevance_score": "0.273399",
                    "ticker_sentiment_score": "0.150571",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Better Growth Stock in 2024: Amazon vs. Apple",
            "url": "https://www.fool.com/investing/2024/01/02/better-growth-stock-in-2024-amazon-vs-apple/",
            "time_published": "20240102T100500",
            "authors": [
                "Dani Cook"
            ],
            "summary": "These companies lead some of the most lucrative industries and have bright outlooks in the new year.",
            "banner_image": "https://media.ycharts.com/charts/d1a14a959d55aedad733987ac7d7dfdb.png",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.955357"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.858979"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.356789,
            "overall_sentiment_label": "Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.534565",
                    "ticker_sentiment_score": "0.633563",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.577979",
                    "ticker_sentiment_score": "0.501857",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "WMT",
                    "relevance_score": "0.058188",
                    "ticker_sentiment_score": "0.195002",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "The 2024 Genesis G90 review: A well-appointed, outstanding full-size luxury sedan",
            "url": "https://www.marketwatch.com/story/the-2024-genesis-g90-review-a-well-appointed-outstandingfull-size-luxury-sedan-8b4315bd",
            "time_published": "20240102T100000",
            "authors": [
                "Eric Brandt"
            ],
            "summary": "The Genesis G90 is an appealing full-size luxury sedan with striking styling, a classy, high-tech interior, and the best warranty in its class.",
            "banner_image": "https://images.mktw.net/im-75300696?width=700&height=427",
            "source": "MarketWatch",
            "category_within_source": "Top Stories",
            "source_domain": "www.marketwatch.com",
            "topics": [
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.382737,
            "overall_sentiment_label": "Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "BBY",
                    "relevance_score": "0.031322",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BGOUF",
                    "relevance_score": "0.031322",
                    "ticker_sentiment_score": "0.120692",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "SSNLF",
                    "relevance_score": "0.062597",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.093775",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Value of Elon Musk's X cut by another fidelity writedown, shows report",
            "url": "https://www.business-standard.com/world-news/elon-musk-s-x-value-cut-by-another-fidelity-writedown-shows-report-124010200139_1.html",
            "time_published": "20240102T044735",
            "authors": [
                "Bloomberg"
            ],
            "summary": "Elon Musk's X is now worth less than a third of the price the billionaire paid for the former Twitter Inc., according to Axios citing disclosures by Fidelity, which helped him complete the $44 billion purchase.",
            "banner_image": "https://bsmedia.business-standard.com/_media/bs/img/article/2024-01/02/full/1704170486-6784.jpg?im=FitAndFill=(826,465)",
            "source": "Business Standard",
            "category_within_source": "GoogleRSS",
            "source_domain": "www.business-standard.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.033956,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.155451",
                    "ticker_sentiment_score": "-0.009748",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.155451",
                    "ticker_sentiment_score": "-0.009748",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Tim Cook Surprises Apple Watch Users With Personal Responses To Life-Saving Stories - Apple  ( NASDAQ:AAPL ) ",
            "url": "https://www.benzinga.com/news/24/01/36445675/tim-cook-surprises-apple-watch-users-with-personal-responses-to-life-saving-stories",
            "time_published": "20240102T030116",
            "authors": [
                "Benzinga Neuro"
            ],
            "summary": "In a surprising turn of events, users of the Apple Watch were met with personal responses from Apple Inc. AAPL CEO Tim Cook after they shared their life-saving experiences with the device via email.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2024/Apples-keynote-event-Tim-Cook-03252019.jpeg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "News",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "1.0"
                }
            ],
            "overall_sentiment_score": 0.284449,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.868151",
                    "ticker_sentiment_score": "0.493686",
                    "ticker_sentiment_label": "Bullish"
                }
            ]
        },
        {
            "title": "Wedbush's Dan Ives Says, 'Tech Stocks Will Be Up 25% In 2024' - Predicts Nasdaq At 20K - Alphabet  ( NASDAQ:GOOG ) , Apple  ( NASDAQ:AAPL ) ",
            "url": "https://www.benzinga.com/markets/equities/24/01/36445586/wedbushs-dan-ives-says-tech-stocks-will-be-up-25-in-2024-predicts-nasdaq-at-20k",
            "time_published": "20240102T020046",
            "authors": [
                "Benzinga Neuro"
            ],
            "summary": "Wedbush analyst Dan Ives projects a 25% surge in tech stocks for 2024, with NASDAQ potentially hitting the 20,000 mark.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2024/tech-stocks.jpeg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "Markets",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.161647"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.262607,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.246999",
                    "ticker_sentiment_score": "0.181472",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "GOOG",
                    "relevance_score": "0.246999",
                    "ticker_sentiment_score": "0.181472",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.166169",
                    "ticker_sentiment_score": "0.286647",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.246999",
                    "ticker_sentiment_score": "0.181472",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "PLTR",
                    "relevance_score": "0.166169",
                    "ticker_sentiment_score": "0.286647",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Buffett's Bullseye: Meet The 4 Stocks That Make Up Nearly 75% Of His Portfolio - Apple  ( NASDAQ:AAPL ) , American Express  ( NYSE:AXP ) ",
            "url": "https://www.benzinga.com/general/24/01/36444463/buffetts-bullseye-meet-the-4-stocks-that-make-up-nearly-75-of-his-portfolio",
            "time_published": "20240101T170014",
            "authors": [
                "Aditi Ganguly"
            ],
            "summary": "Legendary investor Warren Buffett has long preached the importance of passive investing in large-cap stocks. \"Beware the investment activity that produces applause. the great moves are usually greeted by yawns,\" said Buffett, who also is a big fan of dividend-yielding stocks, which he calls the ...",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2024/Warren-Buffett-Amazon-Apple.jpeg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "General",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999897"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.992549"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.268332,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AXP",
                    "relevance_score": "0.28664",
                    "ticker_sentiment_score": "0.152041",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.375722",
                    "ticker_sentiment_score": "0.209837",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "BAC",
                    "relevance_score": "0.28664",
                    "ticker_sentiment_score": "0.223265",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "KO",
                    "relevance_score": "0.28664",
                    "ticker_sentiment_score": "0.213213",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "MS",
                    "relevance_score": "0.04882",
                    "ticker_sentiment_score": "-0.10506",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BRK-A",
                    "relevance_score": "0.14573",
                    "ticker_sentiment_score": "0.257158",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Tesla Near Buy Points But China Rival Is The New BEV King",
            "url": "https://www.investors.com/news/tesla-vs-byd-2024-tsla-stock-ev-rivals/",
            "time_published": "20240101T154800",
            "authors": [
                "ED CARSON",
                "Investor's Business Daily"
            ],
            "summary": "Tesla ( TSLA ) and BYD ( BYDDF ) are the world's largest electric-vehicle makers, becoming more direct competitors in China and much of the world. A lot of attention is focused on EV startups such as Nio ( NIO ) , Li Auto ( LI ) , Xpeng ( XPEV ) , Rivian ( RIVN ) and Lucid ( LCID ) .",
            "banner_image": "https://www.investors.com/wp-content/uploads/2023/11/wTESLAvs110123.jpg",
            "source": "Investors Business Daily",
            "category_within_source": "n/a",
            "source_domain": "www.investors.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Real Estate & Construction",
                    "relevance_score": "0.25"
                }
            ],
            "overall_sentiment_score": -0.007208,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "XPEV",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "0.057866",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "PRBZF",
                    "relevance_score": "0.01054",
                    "ticker_sentiment_score": "0.04584",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "0.093237",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BYDDF",
                    "relevance_score": "0.042141",
                    "ticker_sentiment_score": "0.040745",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "F",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "0.057866",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "GM",
                    "relevance_score": "0.031612",
                    "ticker_sentiment_score": "0.075692",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BRK-A",
                    "relevance_score": "0.01054",
                    "ticker_sentiment_score": "0.0238",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "RIVN",
                    "relevance_score": "0.031612",
                    "ticker_sentiment_score": "0.075692",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "LCID",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "0.057866",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.69717",
                    "ticker_sentiment_score": "-0.030722",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "JBL",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "0.093237",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NIO",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "0.057866",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "PCRFF",
                    "relevance_score": "0.01054",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "PEP",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "SZIHF",
                    "relevance_score": "0.01054",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "LI",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "0.057866",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "FOREX:EUR",
                    "relevance_score": "0.021078",
                    "ticker_sentiment_score": "-0.034208",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Investing Preview 2024: Buy These 4 \"Magnificent Seven\" Stocks. Avoid the Others.",
            "url": "https://www.fool.com/investing/2024/01/01/buy-only-these-4-magnificent-seven-stocks-in-2024/",
            "time_published": "20240101T132100",
            "authors": [
                "Justin Pope"
            ],
            "summary": "The \"Magnificent Seven\" stocks have varying valuations. Four have room to run, and three have gotten too rich.",
            "banner_image": "https://media.ycharts.com/charts/c74e44bc8f9b54f4bbf35ae6fb5010c0.png",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.999499"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.999687"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.263178,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.263942",
                    "ticker_sentiment_score": "0.353315",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "GOOG",
                    "relevance_score": "0.114865",
                    "ticker_sentiment_score": "0.156496",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "META",
                    "relevance_score": "0.076724",
                    "ticker_sentiment_score": "0.186637",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.114865",
                    "ticker_sentiment_score": "0.157204",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.152741",
                    "ticker_sentiment_score": "0.157071",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.263942",
                    "ticker_sentiment_score": "0.227965",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.227361",
                    "ticker_sentiment_score": "0.260211",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Which \"Magnificent Seven\" Stocks Are Screaming Buys Right Now?",
            "url": "https://www.fool.com/investing/2024/01/01/which-magnificent-seven-stocks-are-screaming-buys/",
            "time_published": "20240101T123000",
            "authors": [
                "Keithen Drury"
            ],
            "summary": "Only three of the seven make the cut as buys at current levels.",
            "banner_image": "https://media.ycharts.com/charts/83c00e72f98fcb69a222b796e64f9edd.png",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Economy - Fiscal",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.503496"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.928769"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.198975,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.306325",
                    "ticker_sentiment_score": "0.225847",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "META",
                    "relevance_score": "0.156123",
                    "ticker_sentiment_score": "-0.009425",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.306325",
                    "ticker_sentiment_score": "0.107719",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.400531",
                    "ticker_sentiment_score": "0.086097",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.400531",
                    "ticker_sentiment_score": "0.246622",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.25726",
                    "ticker_sentiment_score": "0.34176",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Should TCW Transform 500 ETF  ( VOTE )  Be on Your Investing Radar?",
            "url": "https://www.zacks.com/stock/news/2204022/should-tcw-transform-500-etf-vote-be-on-your-investing-radar",
            "time_published": "20240101T112007",
            "authors": [
                "Zacks Equity Research"
            ],
            "summary": "Style Box ETF report for VOTE ...",
            "banner_image": "https://staticx-tuner.zacks.com/images/default_article_images/default27.jpg",
            "source": "Zacks Commentary",
            "category_within_source": "n/a",
            "source_domain": "www.zacks.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                }
            ],
            "overall_sentiment_score": 0.159484,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.134968",
                    "ticker_sentiment_score": "0.068008",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.134968",
                    "ticker_sentiment_score": "0.068008",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "MORN",
                    "relevance_score": "0.067727",
                    "ticker_sentiment_score": "0.0",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "10 Stock Market Predictions for 2024",
            "url": "https://www.fool.com/investing/2024/01/01/10-stock-market-predictions-for-2024/",
            "time_published": "20240101T100600",
            "authors": [
                "Sean Williams"
            ],
            "summary": "Here's what to expect from the stock market, the U.S. economy, and some of the most widely held companies in the new year.",
            "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F759652%2Fbear-market-stock-chart-quarter-report-financial-metrics-invest-getty.jpg&op=resize&w=700",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Energy & Transportation",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Blockchain",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.990678"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.769861"
                },
                {
                    "topic": "Real Estate & Construction",
                    "relevance_score": "0.25"
                }
            ],
            "overall_sentiment_score": 0.01223,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.10184",
                    "ticker_sentiment_score": "0.102712",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.040829",
                    "ticker_sentiment_score": "-0.036354",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.081552",
                    "ticker_sentiment_score": "0.12968",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.081552",
                    "ticker_sentiment_score": "0.048932",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AGNC",
                    "relevance_score": "0.061211",
                    "ticker_sentiment_score": "0.16347",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "NLY",
                    "relevance_score": "0.061211",
                    "ticker_sentiment_score": "0.16347",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "NEE",
                    "relevance_score": "0.020421",
                    "ticker_sentiment_score": "0.151454",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "What to stream in January 2024: 'Masters of the Air,' 'Echo,' 'Griselda' and more",
            "url": "https://www.marketwatch.com/story/heres-whats-worth-streaming-in-january-2024-masters-of-the-air-echo-griselda-and-more-2ee21560",
            "time_published": "20231231T211600",
            "authors": [
                "Mike Murphy"
            ],
            "summary": "As the calendar flips to 2024, the streaming world looks more expensive and less expansive than a year ago.",
            "banner_image": "https://images.mktw.net/im-64313763/social",
            "source": "MarketWatch",
            "category_within_source": "Top Stories",
            "source_domain": "www.marketwatch.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.056158,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "NFLX",
                    "relevance_score": "0.108141",
                    "ticker_sentiment_score": "0.056923",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "WBD",
                    "relevance_score": "0.072217",
                    "ticker_sentiment_score": "0.058011",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.060206",
                    "ticker_sentiment_score": "-0.018142",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "PARA",
                    "relevance_score": "0.024102",
                    "ticker_sentiment_score": "0.016712",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.072217",
                    "ticker_sentiment_score": "-0.027629",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "3 Warren Buffett Dividend Growth Stocks to Buy Now and Hold Forever",
            "url": "https://www.fool.com/investing/2023/12/31/3-warren-buffett-dividend-growth-stocks-to-buy-now/",
            "time_published": "20231231T150000",
            "authors": [
                "Adam Levy"
            ],
            "summary": "These three stocks can keep growing their dividends at a great pace for years to come.",
            "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F759631%2Fbuffett2-tmf.jpg&op=resize&w=700",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.962106"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.947132"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.366263,
            "overall_sentiment_label": "Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "TMUS",
                    "relevance_score": "0.081276",
                    "ticker_sentiment_score": "0.096784",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.240489",
                    "ticker_sentiment_score": "0.225259",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "MA",
                    "relevance_score": "0.12165",
                    "ticker_sentiment_score": "0.042878",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "V",
                    "relevance_score": "0.279015",
                    "ticker_sentiment_score": "0.214685",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "BRK-A",
                    "relevance_score": "0.040691",
                    "ticker_sentiment_score": "0.100149",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Almost Half of Warren Buffett-led Berkshire Hathaway's $370 Billion Portfolio Is Invested in Only 1 Stock",
            "url": "https://www.fool.com/investing/2023/12/31/half-warren-buffett-portfolio-invested-in-1-stock/",
            "time_published": "20231231T145300",
            "authors": [
                "Neil Patel"
            ],
            "summary": "This well-known business has been one of the best investments for the conglomerate.",
            "banner_image": "https://g.foolcdn.com/editorial/images/759575/buffett21-tmf.png",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.413559"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.538269"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.231095,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AXP",
                    "relevance_score": "0.06697",
                    "ticker_sentiment_score": "0.18865",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.725359",
                    "ticker_sentiment_score": "0.424969",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "KO",
                    "relevance_score": "0.06697",
                    "ticker_sentiment_score": "0.18865",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "BRK-A",
                    "relevance_score": "0.13347",
                    "ticker_sentiment_score": "0.188494",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Why Artificial Intelligence  ( AI )  Could Be a Game Changer for This \"Magnificent Seven\" Stock",
            "url": "https://www.fool.com/investing/2023/12/31/why-artificial-intelligence-could-be-game-changer/",
            "time_published": "20231231T123000",
            "authors": [
                "Harsh Chauhan"
            ],
            "summary": "This tech titan hasn't benefited from the growing adoption of AI yet, but that could change in the new year.",
            "banner_image": "https://g.foolcdn.com/editorial/images/759445/people-using-smartphone.jpg",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.316726"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.998311"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.236511,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.045224",
                    "ticker_sentiment_score": "0.160039",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "META",
                    "relevance_score": "0.045224",
                    "ticker_sentiment_score": "0.160039",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.045224",
                    "ticker_sentiment_score": "0.160039",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.63579",
                    "ticker_sentiment_score": "0.304027",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.045224",
                    "ticker_sentiment_score": "0.160039",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "$10,000 Invested in This Growth Stock Could Make You a Fortune Over the Next 10 Years",
            "url": "https://www.fool.com/investing/2023/12/31/10000-invested-in-this-growth-stock-could-make-you/",
            "time_published": "20231231T103000",
            "authors": [
                "RJ Fulton"
            ],
            "summary": "As the cryptocurrency market matures, could Coinbase's strategic advancements make it the next success story for investors?",
            "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F759565%2Fwindfall-dividend-payment-happy-investor.jpg&op=resize&w=700",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.360215"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.938793"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Blockchain",
                    "relevance_score": "0.769861"
                }
            ],
            "overall_sentiment_score": 0.186947,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.053509",
                    "ticker_sentiment_score": "0.186986",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.053509",
                    "ticker_sentiment_score": "0.186986",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "COIN",
                    "relevance_score": "0.746105",
                    "ticker_sentiment_score": "0.356143",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "CRYPTO:BTC",
                    "relevance_score": "0.053509",
                    "ticker_sentiment_score": "0.1067",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "China Baidu ERNIE Bot Now Ranking As The #1 Chinese AI Chatbot",
            "url": "https://www.forbes.com/sites/cindygordon/2023/12/30/china-baidu-ernie-bot-now-ranking-as-the-1-chinese-ai-chatbot/",
            "time_published": "20231230T222554",
            "authors": [
                "Cindy Gordon"
            ],
            "summary": "There has been a lot of publicity on generative AI \"chat bot\" innovations across North America. OpenAI's ChatGPT4, Google's Bard, and most recently AmazonQ are all at the competitive generative AI trough.",
            "banner_image": "https://imageio.forbes.com/specials-images/imageserve/659092aee9b5d5ea46f32d84/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds",
            "source": "Forbes",
            "category_within_source": "n/a",
            "source_domain": "www.forbes.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.538269"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.308279,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.241684",
                    "ticker_sentiment_score": "0.270171",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "GOOG",
                    "relevance_score": "0.122269",
                    "ticker_sentiment_score": "0.232785",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.040899",
                    "ticker_sentiment_score": "0.220315",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.040899",
                    "ticker_sentiment_score": "0.024969",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BNS",
                    "relevance_score": "0.040899",
                    "ticker_sentiment_score": "0.19934",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "MS",
                    "relevance_score": "0.040899",
                    "ticker_sentiment_score": "0.220315",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "BIDU",
                    "relevance_score": "0.122269",
                    "ticker_sentiment_score": "0.203965",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "This \"Magnificent Seven\" Stock Is Up 120% in 2023. Here's a 2024 Red Flag Investors Must Know About",
            "url": "https://www.fool.com/investing/2023/12/30/this-magnificent-seven-stock-is-up-120-in-2023-her/",
            "time_published": "20231230T173000",
            "authors": [
                "Justin Pope"
            ],
            "summary": "Tesla's price cuts have lowered margins and earnings growth estimates for the coming years.",
            "banner_image": "https://media.ycharts.com/charts/18176b61ba5a3e918e512c1b1dc46199.png",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.962106"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.9545"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.022227,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.068112",
                    "ticker_sentiment_score": "0.240255",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "META",
                    "relevance_score": "0.068112",
                    "ticker_sentiment_score": "0.240255",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "NVDA",
                    "relevance_score": "0.068112",
                    "ticker_sentiment_score": "0.240255",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.068112",
                    "ticker_sentiment_score": "0.240255",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.76853",
                    "ticker_sentiment_score": "0.020279",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.068112",
                    "ticker_sentiment_score": "0.240255",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Tesla, Apple, Microsoft, Plug Power And Analyst Sees Precursor To Dogecoin Rally: Bulls And Bears",
            "url": "https://www.benzinga.com/trading-ideas/long-ideas/23/12/36433779/benzinga-bulls-and-bears-tesla-apple-microsoft-plug-power-and-analyst-sees-precursor-to-",
            "time_published": "20231230T172340",
            "authors": [
                "Michael Cohen"
            ],
            "summary": "Benzinga examined the prospects for many investors' favorite stocks over the last week - here's a look at some of our top stories. The S&P 500 wrapped up 2023 with a 24% gain, driven by slowing inflation, a strong economy, and the Federal Reserve's hints at ending its rate increases.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2023/12/29/bulls_bears6.png?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "Trading",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Life Sciences",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.839681"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.108179"
                },
                {
                    "topic": "Economy - Macro",
                    "relevance_score": "0.158519"
                }
            ],
            "overall_sentiment_score": 0.237478,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.13459",
                    "ticker_sentiment_score": "0.266239",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "MASI",
                    "relevance_score": "0.13459",
                    "ticker_sentiment_score": "-0.091446",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.265378",
                    "ticker_sentiment_score": "-0.148573",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "PLUG",
                    "relevance_score": "0.13459",
                    "ticker_sentiment_score": "-0.182295",
                    "ticker_sentiment_label": "Somewhat-Bearish"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.200688",
                    "ticker_sentiment_score": "-0.327378",
                    "ticker_sentiment_label": "Somewhat-Bearish"
                },
                {
                    "ticker": "CRYPTO:BTC",
                    "relevance_score": "0.265378",
                    "ticker_sentiment_score": "0.500624",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "CRYPTO:ETH",
                    "relevance_score": "0.13459",
                    "ticker_sentiment_score": "0.328355",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "CRYPTO:DOGE",
                    "relevance_score": "0.265378",
                    "ticker_sentiment_score": "0.285094",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Foldable Phones Battle For Market Share: Samsung Leads, Apple Absent - Apple  ( NASDAQ:AAPL ) , Motorola Solns  ( NYSE:MSI ) ,  ( SSNGY ) ",
            "url": "https://www.benzinga.com/markets/equities/23/12/36438395/foldable-phones-battle-for-market-share-samsung-leads-apple-absent",
            "time_published": "20231230T160324",
            "authors": [
                "Nabaparna Bhattacharya"
            ],
            "summary": "The smartphone industry, excluding Apple Inc. AAPL, is betting on the potential revival of \"foldable\" phones, aiming to breathe life into a sluggish mobile market.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2023/12/30/foldable_phone_shutter.jpg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "General",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.196627,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "SSNLF",
                    "relevance_score": "0.188928",
                    "ticker_sentiment_score": "0.014955",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.28008",
                    "ticker_sentiment_score": "0.202474",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "MSI",
                    "relevance_score": "0.188928",
                    "ticker_sentiment_score": "0.085928",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Oil & Gas Consolidation; Netflix & Disney Partnership; Federal Student Aid Changes",
            "url": "https://www.fool.com/investing/2023/12/30/oil-gas-consolidation-netflix-disney-partnership-f/",
            "time_published": "20231230T155200",
            "authors": [
                "Motley Fool Staff"
            ],
            "summary": "\"Motley Fool Money\" helps you stay up to date.",
            "banner_image": "https://g.foolcdn.com/editorial/images/759026/mfm_12.jpg",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.310843"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.858979"
                },
                {
                    "topic": "Mergers & Acquisitions",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Energy & Transportation",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.180893,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "NFLX",
                    "relevance_score": "0.215625",
                    "ticker_sentiment_score": "0.140286",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "GOOG",
                    "relevance_score": "0.104493",
                    "ticker_sentiment_score": "0.064516",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "OXY",
                    "relevance_score": "0.017464",
                    "ticker_sentiment_score": "0.113591",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.104493",
                    "ticker_sentiment_score": "0.071822",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "SPOT",
                    "relevance_score": "0.008733",
                    "ticker_sentiment_score": "0.062137",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "XOM",
                    "relevance_score": "0.008733",
                    "ticker_sentiment_score": "0.038606",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "WBD",
                    "relevance_score": "0.008733",
                    "ticker_sentiment_score": "0.065371",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "PXD",
                    "relevance_score": "0.008733",
                    "ticker_sentiment_score": "0.038606",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "2 Best Warren Buffett Stocks to Buy for the Long Haul",
            "url": "https://www.fool.com/investing/2023/12/30/2-best-warren-buffett-stocks-to-buy-for-the-long/",
            "time_published": "20231230T131500",
            "authors": [
                "Prosper Junior Bakiny"
            ],
            "summary": "These companies need no introduction.",
            "banner_image": "https://media.ycharts.com/charts/d2c9a30539d16f42d92b7ad1a78a6296.png",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Life Sciences",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.929393"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.360215"
                },
                {
                    "topic": "Mergers & Acquisitions",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.333333"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.333333"
                }
            ],
            "overall_sentiment_score": 0.308892,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.461889",
                    "ticker_sentiment_score": "0.355779",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "BRK-A",
                    "relevance_score": "0.089129",
                    "ticker_sentiment_score": "0.180726",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                },
                {
                    "ticker": "JNJ",
                    "relevance_score": "0.304787",
                    "ticker_sentiment_score": "0.288497",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Would a Macy's Buyout Be a Miracle on 34th Street?",
            "url": "https://www.fool.com/investing/2023/12/30/would-a-macys-buyout-be-a-miracle-on-34th-street/",
            "time_published": "20231230T124300",
            "authors": [
                "Motley Fool Staff"
            ],
            "summary": "Should investors be excited about a big department store potentially going private?",
            "banner_image": "https://g.foolcdn.com/editorial/images/758089/mfm_11.jpg",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Technology",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Retail & Wholesale",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.999858"
                },
                {
                    "topic": "Mergers & Acquisitions",
                    "relevance_score": "0.684621"
                }
            ],
            "overall_sentiment_score": 0.144083,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "TGT",
                    "relevance_score": "0.023191",
                    "ticker_sentiment_score": "0.063376",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "HUM",
                    "relevance_score": "0.015462",
                    "ticker_sentiment_score": "0.006029",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.007731",
                    "ticker_sentiment_score": "0.052115",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BAC",
                    "relevance_score": "0.007731",
                    "ticker_sentiment_score": "-0.002517",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BRK-A",
                    "relevance_score": "0.030918",
                    "ticker_sentiment_score": "0.054817",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "NKE",
                    "relevance_score": "0.007731",
                    "ticker_sentiment_score": "0.056576",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "KSS",
                    "relevance_score": "0.015462",
                    "ticker_sentiment_score": "0.003451",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "UA",
                    "relevance_score": "0.007731",
                    "ticker_sentiment_score": "0.056576",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "M",
                    "relevance_score": "0.161247",
                    "ticker_sentiment_score": "0.100054",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "MSFT",
                    "relevance_score": "0.007731",
                    "ticker_sentiment_score": "0.065966",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BOC",
                    "relevance_score": "0.123209",
                    "ticker_sentiment_score": "0.068177",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AMZN",
                    "relevance_score": "0.023191",
                    "ticker_sentiment_score": "0.072183",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "WMT",
                    "relevance_score": "0.015462",
                    "ticker_sentiment_score": "0.060206",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "Was FedEx's Quarter Really That Bad? Was the Comcast Data Breach Really Not That Bad?",
            "url": "https://www.fool.com/investing/2023/12/30/was-fedexs-quarter-really-that-bad-was-the-comcast/",
            "time_published": "20231230T121500",
            "authors": [
                "Motley Fool Staff"
            ],
            "summary": "We also chat with Kristy Akullian, senior member of the iShares investment strategy team at BlackRock, for a look at what's coming for 2024.",
            "banner_image": "https://g.foolcdn.com/editorial/images/759034/mfm_20.jpg",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Energy & Transportation",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Finance",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Economy - Monetary",
                    "relevance_score": "0.769861"
                },
                {
                    "topic": "Economy - Fiscal",
                    "relevance_score": "0.310843"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.25"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.576289"
                }
            ],
            "overall_sentiment_score": 0.104525,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "BLK",
                    "relevance_score": "0.021022",
                    "ticker_sentiment_score": "-0.015378",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.135995",
                    "ticker_sentiment_score": "0.033556",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "CRWD",
                    "relevance_score": "0.010512",
                    "ticker_sentiment_score": "-0.080979",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "ZS",
                    "relevance_score": "0.021022",
                    "ticker_sentiment_score": "-0.032028",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "CCZ",
                    "relevance_score": "0.115232",
                    "ticker_sentiment_score": "-0.013672",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "FDX",
                    "relevance_score": "0.073482",
                    "ticker_sentiment_score": "0.043723",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "BA",
                    "relevance_score": "0.010512",
                    "ticker_sentiment_score": "0.099407",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "This Is Warren Buffett's Favorite Artificial Intelligence  ( AI )  Stock. Here's Why.",
            "url": "https://www.fool.com/investing/2023/12/30/this-is-warren-buffetts-favorite-artificial-intell/",
            "time_published": "20231230T110500",
            "authors": [
                "Adam Levy"
            ],
            "summary": "Warren Buffett approaches AI with some trepidation, but he has bet big on this leading innovator.",
            "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F759625%2Fbuffett11-tmf.jpg&op=resize&w=700",
            "source": "Motley Fool",
            "category_within_source": "n/a",
            "source_domain": "www.fool.com",
            "topics": [
                {
                    "topic": "Earnings",
                    "relevance_score": "0.158519"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "1.0"
                },
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.995077"
                }
            ],
            "overall_sentiment_score": 0.279228,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.510043",
                    "ticker_sentiment_score": "0.361173",
                    "ticker_sentiment_label": "Bullish"
                }
            ]
        },
        {
            "title": "Gary Black Says Apple Should Buy Rivian To Catch Up With Chinese Smartphone Rivals Making Cars - Rivian Automotive  ( NASDAQ:RIVN ) ",
            "url": "https://www.benzinga.com/news/23/12/36437159/gary-black-says-apple-should-buy-rivian-to-catch-up-with-chinese-smartphone-rivals-making-cars",
            "time_published": "20231230T043929",
            "authors": [
                "Anan Ashraf"
            ],
            "summary": "Future Fund Managing Partner Gary Black on Friday opined that tech giant Apple Inc AAPL must try to buy California-based EV startup Rivian Automotive Inc RIVN given that Chinese smartphone makers are overtaking it in producing cars.",
            "banner_image": "https://cdn.benzinga.com/files/images/story/2023/Apple-Shutterstock_11.jpeg?width=1200&height=800&fit=crop",
            "source": "Benzinga",
            "category_within_source": "News",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Earnings",
                    "relevance_score": "0.360215"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.151426,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "RIVN",
                    "relevance_score": "0.829487",
                    "ticker_sentiment_score": "0.378029",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.639128",
                    "ticker_sentiment_score": "0.274151",
                    "ticker_sentiment_label": "Somewhat-Bullish"
                }
            ]
        },
        {
            "title": "Billionaire Gustavo Cisneros, who defined Venezuela business, dies at 78",
            "url": "https://www.business-standard.com/world-news/billionaire-gustavo-cisneros-who-defined-venezuela-business-dies-at-78-123123000091_1.html",
            "time_published": "20231230T033642",
            "authors": [
                "Bloomberg"
            ],
            "summary": "Gustavo Cisneros, an entrepreneur who brought US multinational businesses to Venezuela and oversaw a broad array of assets from media to industry, has died. He was 78. Click here to follow our WhatsApp channel His death was confirmed by the Cisneros Group, without providing additional details.",
            "banner_image": "https://bsmedia.business-standard.com/_media/bs/img/article/2023-12/30/full/1703907388-9177.jpeg?im=FeatureCrop,size=(826,465)",
            "source": "Business Standard",
            "category_within_source": "GoogleRSS",
            "source_domain": "www.business-standard.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.360215"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Mergers & Acquisitions",
                    "relevance_score": "0.108179"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.049665,
            "overall_sentiment_label": "Neutral",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.066598",
                    "ticker_sentiment_score": "0.09418",
                    "ticker_sentiment_label": "Neutral"
                },
                {
                    "ticker": "PEP",
                    "relevance_score": "0.066598",
                    "ticker_sentiment_score": "0.09418",
                    "ticker_sentiment_label": "Neutral"
                }
            ]
        },
        {
            "title": "CEO Elon Musk Reiterates Tesla Market Cap Could Surpass Apple, Saudi Aramco Combined In Next 5 Years: 'If...Executes Extremely Well' - Tesla  ( NASDAQ:TSLA ) ",
            "url": "https://www.benzinga.com/markets/equities/23/12/36437025/ceo-elon-musk-reiterates-tesla-market-cap-could-surpass-apple-saudi-aramco-combined-in-next-5-ye",
            "time_published": "20231230T030146",
            "authors": [
                "Anan Ashraf"
            ],
            "summary": "Tesla Inc TSLA CEO Elon Musk on Friday reiterated his prediction that his EV company's long-term value could exceed both tech giant Apple Inc AAPL and Saudi Aramco put together.",
            "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png",
            "source": "Benzinga",
            "category_within_source": "Markets",
            "source_domain": "www.benzinga.com",
            "topics": [
                {
                    "topic": "Financial Markets",
                    "relevance_score": "0.108179"
                },
                {
                    "topic": "Manufacturing",
                    "relevance_score": "0.5"
                },
                {
                    "topic": "Earnings",
                    "relevance_score": "0.495866"
                },
                {
                    "topic": "Technology",
                    "relevance_score": "0.5"
                }
            ],
            "overall_sentiment_score": 0.188869,
            "overall_sentiment_label": "Somewhat-Bullish",
            "ticker_sentiment": [
                {
                    "ticker": "AAPL",
                    "relevance_score": "0.457566",
                    "ticker_sentiment_score": "0.482811",
                    "ticker_sentiment_label": "Bullish"
                },
                {
                    "ticker": "TSLA",
                    "relevance_score": "0.713572",
                    "ticker_sentiment_score": "0.404687",
                    "ticker_sentiment_label": "Bullish"
                }
            ]
        }
    ]
}

for i in range(len(NEWS['feed'])):
    print(NEWS['feed'][i]['title'])

print('===============================================')


# ticker_list = ["A", "AL", "AAP", "AAPL", "ZBRA", "ZION", "ZTS"]
# all_symbols = " ".join(ticker_list)
# myInfo = Ticker(all_symbols)
# myDict = myInfo.price

# for ticker in ticker_list:
#     ticker = str(ticker)
#     longName = myDict[ticker]['longName']
#     market_cap = myDict[ticker]['marketCap']
#     price = myDict[ticker]['regularMarketPrice']
#     print(ticker, market_cap, price)

aapl = Ticker('aapl')
print(aapl.summary_detail)




