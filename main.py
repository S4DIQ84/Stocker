import requests
from twilio.rest import Client
import datetime as dt

STOCK = "Stock Name"
COMPANY_NAME = "Company Name"

#Alpha API
alpha_api = "https://www.alphavantage.co/query?"
alpha_api_key = ""

#News API
news_api = "https://newsapi.org/v2/top-headlines"
news_api_key = ""

#Twilio Tokens
account_sid = ''
auth_token = ''



client = Client(account_sid, auth_token)
today = dt.date.today() - dt.timedelta(days=1)
day_before_yesterday = today - dt.timedelta(days=1 )
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api_key
}
response = requests.get(url=alpha_api, params=parameters)
data = response.json()
# market close values
previous_say_close = float(data["Time Series (Daily)"][f"{today}"]["4. close"])
dby_close = float(data["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"])
close_diff = float(previous_say_close) - float(dby_close)
print(data)

close_percent = (close_diff/float(previous_say_close))*100
percent = "{:.2f}%".format(close_percent)

news_parameters = {
    "apiKey": news_api_key,
    "q": "Company Name",
    "category": ["business", "general", "technology"],
    "language": "en"
}
news_response = requests.get(url=news_api, params=news_parameters)
news = news_response.json()
news_articles = news['articles']
news_title = news["articles"][0]["title"]
news_desc = news["articles"][0]["description"]

if previous_say_close < dby_close:
    symbol = "🔻"
else:
    symbol = "🔺"

for article in news_articles:
    print(article["title"])
    txt_msg = f"{STOCK}:{symbol}{percent}\nHeadline: {article['title']}\nBrief: {article['description']}"
    message = client.messages.create(
        from_="Twilio Number",
        to= "Reciver Number",
        body=txt_msg
        )
    print(message.sid)
    print(txt_msg)
