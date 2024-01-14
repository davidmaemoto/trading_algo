import alpaca_trade_api as tradeapi
import medianInvest as medianBot

# authentication and connection details
api_key = 'PKIXSKAD4YF786NW2Q61'
api_secret = 'g2bmgR2wPRkzH5eP27hsPZRu8OQSKOw4dbOegfRT'
base_url = 'https://paper-api.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# obtain account information
account = api.get_account()
print(account)

bot = medianBot(api_key, api_secret, base_url)
bot.run()