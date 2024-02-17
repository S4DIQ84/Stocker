# Stock Price and News Notifier

## Overview
This script fetches stock price data for Tesla Inc. (TSLA) from Alpha Vantage API, checks for significant price changes, retrieves news articles related to Tesla using News API, and sends notifications via Twilio to a specified phone number.

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
An example SMS notification:
