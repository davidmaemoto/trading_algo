import alpaca_trade_api as tradeapi
import time
import datetime



class medianBot:
    def __init__(self, api_key, api_secret, base_url, symbol):
        self.api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
        self.symbol = symbol
        self.last_updated_month = datetime.datetime.now().month

    def predict_median_price(self):
        # Add logic to predict the median price of the stock
        pass


    def rebalance_trades(self, median_price):
        # Add logic to re-buy or re-short the stock when the price crosses the median price
        pass

    def calculate_moving_average(self, symbol, window):
        # Fetch historical data
        barset = self.api.get_barset(symbol, 'day', limit=window)
        bars = barset[symbol]
        # Calculate average
        average_price = sum([bar.c for bar in bars]) / len(bars)
        return average_price
    
    def set_trailing_stop_loss(self, symbol, current_price, trailing_percent):
        # Calculate the stop-loss price based on the trailing percentage
        stop_loss_price = current_price * (1 - trailing_percent / 100)
        return stop_loss_price

    def analyze_volume(self, symbol):
        # Fetch latest trading volume
        barset = self.api.get_barset(symbol, 'day', limit=1)
        last_bar = barset[symbol][0]
        return last_bar.v

    def should_enter_trade(self, median_price, current_price, volume):
        # Example logic: Enter trade if volume is above a certain threshold
        volume_threshold = 100000 # Set your volume threshold
        if volume > volume_threshold:
            if current_price < median_price:
                # If current price is below median, consider buying
                return 'buy'
            elif current_price > median_price:
                # If current price is above median, consider selling
                return 'sell'
        return 'hold'

    def execute_trade(self):
        median_price = self.predict_median_price()
        current_price = self.get_current_price()
        volume = self.analyze_volume()

        decision = self.should_enter_trade(median_price, current_price, volume)
        if decision == 'buy':
            # Implement buy logic
            pass
        elif decision == 'sell':
            # Implement sell logic
            pass
        elif decision == 'hold':
            # Implement hold logic
            pass

    def get_current_price(self):
        # Implement logic to fetch the current price of the stock
        pass

    def run(self):
        while True:
            time.sleep(1) # Adjust the sleep time as needed
            median_price = self.predict_median_price()
            self.execute_trade(median_price)
            self.rebalance_trades(median_price)
