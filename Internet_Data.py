import urllib.request

nasdaqAppleUrl = 'https://www.nasdaq.com/market-activity/stocks/aapl'
connection = urllib.request.urlopen(nasdaqAppleUrl)
responseString = connection.read().decode()
print(responseString)
