# Scrapes Wikipedia page for list of SP 500 companies
# and queries Yahoo finance to save the historical data for tickers.
# Author: Kiran Bhattacharyya
# License: MIT License

import urllib2
import pytz
import pandas_datareader.data as web
import datetime
from bs4 import BeautifulSoup
import csv


#### Section 1: Scrapes wikipedia page to get all tickers in the S&P 500
thisurl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

myPage = urllib2.urlopen(thisurl)

mySoup = BeautifulSoup(myPage, "html.parser")

table = mySoup.find('table', {'class': 'wikitable sortable'})

sector_tickers = dict()
for row in table.findAll('tr'):
    col = row.findAll('td')
    if len(col) > 0:
        sector = str(col[3].string.strip()).lower().replace(' ', '_')
        ticker = str(col[0].string.strip())
        if sector not in sector_tickers:
            sector_tickers[sector] = list()
        sector_tickers[sector].append(ticker)

#### Section 2: Queries Yahoo Finance for historical data on tickers
# Start and end dates for historical data
start = datetime.datetime(2010, 1, 1)  # start date
end = datetime.datetime(2016, 12, 27) # end date

myKeys = sector_tickers.keys()

for i in xrange(0,len(myKeys)):
    myTickers = sector_tickers[myKeys[i]]
    for j in xrange(0,len(myTickers)):
        myData = web.DataReader(myTickers[j], 'yahoo', start, end)
        fileName = myTickers[j] + '.csv'
        myData.to_csv(fileName)
