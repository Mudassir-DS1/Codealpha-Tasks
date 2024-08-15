import requests
import pandas as pd

API_KEY = 'your_alpha_vantage_api_key'
BASE_URL = 'https://www.alphavantage.co/query'

portfolio = {}

def get_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Time Series (1min)' in data:
        latest_time = list(data['Time Series (1min)'].keys())[0]
        return float(data['Time Series (1min)'][latest_time]['1. open'])
    else:
        return None

def add_stock(symbol, shares):
    price = get_stock_price(symbol)
    if price:
        portfolio[symbol] = {'shares': shares, 'price': price}
        print(f"Added {shares} shares of {symbol} at ${price:.2f} each.")
    else:
        print(f"Failed to retrieve data for {symbol}.")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")

def view_portfolio():
    df = pd.DataFrame(portfolio).T
    df['total_value'] = df['shares'] * df['price']
    print(df)

# Main loop
while True:
    print("\nOptions: add, remove, view, exit")
    choice = input("Choose an option: ").strip().lower()
    if choice == 'add':
        symbol = input("Enter stock symbol: ").strip().upper()
        shares = int(input("Enter number of shares: "))
        add_stock(symbol, shares)
    elif choice == 'remove':
        symbol = input("Enter stock symbol: ").strip().upper()
        remove_stock(symbol)
    elif choice == 'view':
        view_portfolio()
    elif choice == 'exit':
        break
    else:
        print("Invalid option. Please try again.")
