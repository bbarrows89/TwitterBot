import tweepy, requests, time, os

# Use python time.sleep(sec) to set an interval of a half hour.
INTERVAL = 60 * 30
CMC_PRO_API_KEY = os.environ.get('CMC_KEY')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

# Use Tweepy to submit API keys and interface with Twitter API.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterAPI = tweepy.API(auth)

def get_bitcoin():
    # define CoinMarketCap API usage
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    # Feed my API key and use the "symbol" query to only return BTC prices.
    headers = {'X-CMC_PRO_API_KEY': CMC_PRO_API_KEY}
    params = {'symbol' : 'BTC'}
    
    # Make GET request and parse the JSON structure to retrieve the quote response.
    r = requests.get(url, headers=headers, params=params).json()
    print(r)
    quote_json = r['data']['BTC']['quote']['USD']
   
   # Collect relevant data into dict
    percentage_changes = {
        'hour': quote_json['percent_change_1h'],
        'day': quote_json['percent_change_24h'],
        'week': quote_json['percent_change_7d']
    }

  
    duration = ''
    price = str(round(quote_json['price'], 2)
    message = ''
    
    # create message based upon price movement
    for name, amt in percentage_changes.items():
        if amt >= 10:
            amount = str(round(amt, 2))
            duration = name
            message = "#BTC has risen by {}% in the last {}. The price is currently ${}.".format(amount, name, price)
        elif amt <= -10:
            amount = str(round(amt, 2))
            duration = name
            message = "#BTC has fallen by {}% in the last {}. The price is currently ${}.".format(amount, name, price)
        else:
            message = ("The current price of #BTC is $" + price + " in USD")

    print(message)
    print(percent_changes)
    return message

def send_tweet(message):
    TwitterAPI.update_status(message)

while True:
    send_tweet(get_bitcoin())
    time.sleep(INTERVAL) 