import tweepy, requests, config, os

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

    # Printing to console for testing purposes
   #  print(quote_json)
    print(percentage_changes['one_hour_percentage_change'])
    return percentage_changes

#get_bitcoin()

'''
def check_price():
    rise_message = (f"The price of BTC has risen by %" + amount + " in the past " + duration + ".")
    fall_message = (f"The price of BTC has fallen by %" + amount + " in the past " + duration + ".")
    def check_hour(percentage_changes):
        if percentage_changes['one_hour'] >= 5.0:
            print("The price of BTC has risen by %" + percentage_changes['one_hour'] + " in the last hour.")
        elif percentage_changes['one_hour'] <= -5.0:
            print("The price of BTC has fallen by %" + percentage_changes['one_hour'] + " in the last hour.")
    def check_day():
        if percentage_changes['one_day'] >= 10.0:
            message = ("The price of BTC has risen by %" + percentage_changes['one_day'] + " in the last day.")
            print(message)
            return tweet(message)
        elif percentage_changes['one_day'] <= 10.0:
            message = ("The price of BTC has fallen by %" + percentage_changes['one_day'] + " in the last day.")
            print(message)
            return tweet(message)
'''

