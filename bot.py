import tweepy, requests, time, config

# Use python time.sleep(sec) to set an interval of a half hour.
INTERVAL = 60 * 30
CMC_PRO_API_KEY = config.cmc_api

# Use Tweepy to submit API keys and interface with Twitter API.
def setup_tweepy():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    TwitterAPI = tweepy.API(auth)

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
        'one_hour_percentage_change': quote_json['percent_change_1h'],
        'one_day_percentage_change': quote_json['percent_change_24h'],
        'one_week_percentage_change': quote_json['percent_change_7d']
    }

    return percentage_changes
    '''   
    Used for testing responses

    print(quote_json)
    print(percentage_changes.items())
    '''

get_bitcoin()

#def check_price():
   # if 

