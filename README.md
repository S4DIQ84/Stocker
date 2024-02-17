# Stock Price and News Notifier

## Overview
This script fetches stock price data for a specified stock from Alpha Vantage API, checks for significant price changes, retrieves news articles related to the specified stock using News API, and sends notifications via Twilio to a specified phone number.

## Setup

### Prerequisites
- Python 3.x installed
- `requests` library installed (`pip install requests`)
- `twilio` library installed (`pip install twilio`)
- Alpha Vantage API key
- News API key
- Twilio account SID and authentication token

### Installation
1. Clone this repository: `git clone https://github.com/yourusername/stock-news-notifier.git`
2. Navigate to the project directory: `cd stock-news-notifier`
3. Install required dependencies: `pip install -r requirements.txt`

### Configuration
1. Obtain an API key from [Alpha Vantage](https://www.alphavantage.co/) and replace `alpha_api_key` in the script with your API key.
2. Obtain an API key from [News API](https://newsapi.org/) and replace `news_api_key` in the script with your API key.
3. Set up a Twilio account and obtain your account SID and authentication token. Replace `account_sid` and `auth_token` in the script with your credentials.
4. Update the `to` field in the `client.messages.create()` method with your phone number.

## Usage
1. Run the script: `python stock_news_notifier.py`
2. Receive notifications on your phone with stock price changes and related news articles.

## Example
TSLA:🔻-0.25%
Headline: Tesla may head to India on incentive-paved road - The Economic Times
Brief: India imposes 100% import duty on cars with cost, insurance and freight value of more than $40,000 (about Rs 33 lakh), and 60% for those below that threshold. Tesla is willing to invest up to $2 billion if the Indian government offers reduced import duty of 1…

## License
This project is licensed under the [MIT License](LICENSE).

## Contributors
- Mohammed Sadiq Ali(https://github.com/S4DIQ84/)
