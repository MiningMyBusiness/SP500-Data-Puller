# S&P 500 Data Puller
Downloads historical data of all tickers in the S&P 500.

"myWebscraper.py" has two main portions which are described below.

## Section 1: Scrape Wikipedia page with list of S&P 500 companies 
The first part of this code scrapes the relevant wikipedia page to get all the tickers in the S&P 500 according to the market sector and stores it in a python dictionary database. 

## Section 2: Query 'Yahoo Finance' for historical data and save as .csv
The second portion of this code queries 'Yahoo Finance' via the pandas.datareader to get the historical data for the tickers between the dates specified within the code. This data is read into a pandas dataframe structure which is then saved as a .csv for potential use with other programs like R or Excel. 
