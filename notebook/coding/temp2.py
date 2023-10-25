# Python code
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# Get today's date
today = datetime.date.today()

# Get the start of the year
start_of_year = datetime.date(today.year, 1, 1)

# Download the historical data
meta_data = yf.download("FB", start=start_of_year, end=today)
tesla_data = yf.download("TSLA", start=start_of_year, end=today)

# Calculate the YTD return
meta_data["YTD Return"] = (meta_data["Adj Close"] / meta_data["Adj Close"].iloc[0]) - 1
tesla_data["YTD Return"] = (tesla_data["Adj Close"] / tesla_data["Adj Close"].iloc[0]) - 1

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(meta_data["YTD Return"], label="META")
plt.plot(tesla_data["YTD Return"], label="TESLA")
plt.title("META vs TESLA YTD Return")
plt.xlabel("Date")
plt.ylabel("YTD Return")
plt.legend()
plt.grid(True)
plt.show()
