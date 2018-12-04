import tweepy, requests, config, os, time

# Use python time.sleep(sec) to set an interval of a half hour.
INTERVAL = 60 * 30
CMC_PRO_API_KEY = config.keys['cmc_api']

# Use Tweepy to submit API keys and interface with Twitter API.
def setup_tweepy():
    auth = tweepy.OAuthHandler(config.keys['consumer_key'], config.keys['consumer_secret'])
    auth.set_access_token(config.keys['access_token'], config.keys['access_secret'])
    TwitterAPI = tweepy.API(auth)
    return TwitterAPI

def get_bitcoin():
    # define CoinMarketCap API usage
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    # Feed my API key and use the "symbol" query to only return BTC prices.
    headers = {'X-CMC_PRO_API_KEY': CMC_PRO_API_KEY}
    params = {'symbol' : 'BTC'}
    
    # Make GET request and parse the JSON structure to retrieve the quote response.
    r = requests.get(url, headers=headers, params=params).json()
    quote_json = r['data']['BTC']['quote']['USD']
   
   # Collect relevant data into dict
    percentage_changes = {
        'one_hour': quote_json['percent_change_1h'],
        'one_day': quote_json['percent_change_24h'],
        'one_week': quote_json['percent_change_7d']
    }

    duration = ''
    price = 0.0
    message = ''
    
    # create message based upon price movement
    for name, amt in percentage_changes.items():
        if amt >= 10:
            amount = str(round(amt, 2))
            duration = name
            message = "BTC has risen by {}% in the last {}.".format(amount, name)
        elif amt <= -10:
            amount = str(round(amt, 2))
            duration = name
            message = "BTC has fallen by {}% in the last {}.".format(amount, name)
        else:
            message = ("The current price of BTC is $" + str(round(quote_json['price'], 2)) + " in USD")

    print(message)
    return message

def send_tweet(message):
    TwitterAPI.status_update(message)

setup_tweepy()

while True:
    send_tweet(get_bitcoin())
    time.sleep(INTERVAL) 