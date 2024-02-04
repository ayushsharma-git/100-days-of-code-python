import pandas as pd
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_ALPHAADVANTAGE = ""
API_KEY_NEWS = ""

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_ALPHAADVANTAGE
}
response = requests.get(url="https://www.alphavantage.co/query", params=params)
response.raise_for_status()

data = response.json()
print(data)
time_series_df = pd.DataFrame(data["Time Series (Daily)"])

yest_high = float(time_series_df.at["4. close", time_series_df.columns[0]])
day_bef_high = float(time_series_df.at["4. close", time_series_df.columns[1]])

perc = (yest_high - day_bef_high) / day_bef_high
print(f"{STOCK} {round(perc * 100)}%")

if perc > 0.05:
    print("Good news")
else:
    print("No news")

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
params = {
    "q": COMPANY_NAME,
    "apiKey": API_KEY_NEWS
}
response = requests.get(url="https://newsapi.org/v2/everything", params=params)
response.raise_for_status()

news = response.json()
print(news["articles"][0]["title"])
print(news["articles"][0]["description"])

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
