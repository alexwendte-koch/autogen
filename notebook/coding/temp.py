import datetime
import yfinance as yf

# Get the current date
current_date = datetime.date.today()
print("Today's date is:", current_date)

# Define the ticker symbol
tickerSymbols = ["META", "TSLA"]

# Get data on this ticker
for ticker in tickerSymbols:
    tickerData = yf.Ticker(ticker)

    # get historical market data, here max is 5 years.
    tickerDf = tickerData.history(period="1d", start="2022-1-1", end=current_date)

    # calculate the YTD return
    ytd_return = (tickerDf["Close"][-1] - tickerDf["Close"][0]) / tickerDf["Close"][0]

    print(f"The YTD return for {ticker} is {ytd_return * 100}%")
