import pandas as pd
import talib

# Assuming you have historical price data in a pandas DataFrame
# with columns 'timestamp', 'open', 'high', 'low', 'close', 'volume'
data = pd.read_csv('your_data_file.csv')

# Calculate moving averages
data['ma_short'] = talib.SMA(data['close'], timeperiod=50)
data['ma_long'] = talib.SMA(data['close'], timeperiod=200)

# Calculate RSI
data['rsi'] = talib.RSI(data['close'], timeperiod=14)

# Define your strategy logic
def implement_strategy(data):
    positions = []  # To store positions (buy/sell signals)

    for i in range(len(data)):
        # Entry conditions: MA crossover and RSI conditions
        if data['ma_short'][i] > data['ma_long'][i] and data['rsi'][i] < 30:
            positions.append('Buy')
        # Exit conditions: Opposite MA crossover or RSI conditions
        elif data['ma_short'][i] < data['ma_long'][i] or data['rsi'][i] > 70:
            positions.append('Sell')
        else:
            positions.append('Hold')

    data['positions'] = positions

# Call the strategy implementation function
implement_strategy(data)

# Print the resulting DataFrame with positions
print(data)