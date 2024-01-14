import alpaca_trade_api as tradeapi
import time
import datetime



class medianBot:
    def __init__(self, api_key, api_secret, base_url, symbol):
        self.api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
        self.symbol = symbol
        self.last_updated_month = datetime.datetime.now().month

    def predict_median_price(self):
        barset = self.api.get_barset(self.symbol, 'day', limit=30)
        bars = barset[self.symbol]

        # Extract closing prices
        closing_prices = [bar.c for bar in bars]

        # Calculate the median price
        median_price = sorted(closing_prices)[len(closing_prices)//2]

        return median_price

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


    def buy_stock(self, qty):
        # Place a market order to buy the stock
        try:
            self.api.submit_order(
                symbol=self.symbol,
                qty=qty,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            print(f"Buy order placed for {qty} shares.")
        except Exception as e:
            print(f"Error placing buy order: {e}")

    def sell_stock(self, qty):
        # Place a market order to sell the stock
        try:
            self.api.submit_order(
                symbol=self.symbol,
                qty=qty,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            print(f"Sell order placed for {qty} shares.")
        except Exception as e:
            print(f"Error placing sell order: {e}")



    def execute_trade(self):
        median_price = self.predict_median_price()
        current_price = self.get_current_price()
        volume = self.analyze_volume()

        decision = self.should_enter_trade(median_price, current_price, volume)
        if decision == 'buy':
            self.buy_stock{1}
        elif decision == 'sell':
            self.sell_stock{1}
        elif decision == 'hold':
            time.sleep(3600)

    def get_current_price(self):
        try:
            last_trade = self.api.get_last_trade(self.symbol)
            current_price = last_trade.price
            return current_price
        except Exception as e:
            print(f"Error fetching current price: {e}")
            return None


    def run(self):
        while True:
            time.sleep(3600) # Adjust the sleep time as needed
            median_price = self.predict_median_price()
            self.execute_trade(median_price)
