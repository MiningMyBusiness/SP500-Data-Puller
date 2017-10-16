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

thisurl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies" # the wikipedia url containing list of S&P 500 companies
# it helps to visit the webpage and take a look at the source to understand
#    how the html is parsed.

myPage = urllib2.urlopen(thisurl) # opens this url

mySoup = BeautifulSoup(myPage, "html.parser") # parse html soup 

table = mySoup.find('table', {'class': 'wikitable sortable'}) # finds wiki sortable table in webpage html

sector_tickers = dict() # create a dictionary to store all tickers according to sector
for row in table.findAll('tr'): # find every row in the table
    col = row.findAll('td') # find every column in that row
    if len(col) > 0: # if there are columns in that row
        sector = str(col[3].string.strip()).lower().replace(' ', '_') # identify the sector in the row
        ticker = str(col[0].string.strip()) # identify the ticker in the row
        if sector not in sector_tickers: # if this sector is not a key in the dictionary
            sector_tickers[sector] = list() # add this as a key to the dictionary
        sector_tickers[sector].append(ticker) # add the ticker to right key in the dictionary

#### Section 2: Queries Yahoo Finance for historical data on tickers

# Start and end dates for historical data
start = datetime.datetime(2010, 1, 1)  # start date
end = datetime.datetime(2016, 12, 27) # end date

myKeys = sector_tickers.keys() # find all the sectors which are keys in the dictionary we created in Step 1

for i in xrange(0,len(myKeys)): # for each key in the dictionary which represents a sector
    myTickers = sector_tickers[myKeys[i]] # find the tickers in that list
    for j in xrange(0,len(myTickers)): # for each ticker
        myData = web.DataReader(myTickers[j], 'yahoo', start, end) # query the pandas datareader to pull data from Yahoo! finance
        fileName = myTickers[j] + '.csv' # create a file
        myData.to_csv(fileName) # save data to the file
