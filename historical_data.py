from index import init_client
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime


def historical_data(symbol , client):
	symbol+='USDT'
	# Getting earliest timestamp availble (on Binance)
	earliest_timestamp = client._get_earliest_valid_timestamp(symbol, '1d')  # Here "symbol USDT" is a trading pair and "1d" is time interval

	# Getting historical data (candle data or kline)
	candle = client.get_historical_klines(symbol, "1d", earliest_timestamp, limit=1000)

	crypto_df = pd.DataFrame(candle, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
	crypto_df.dateTime = pd.to_datetime(crypto_df.dateTime, unit='ms')
	crypto_df.closeTime = pd.to_datetime(crypto_df.closeTime, unit='ms')
	#crypto_df.set_index('dateTime', inplace=True)
	# crypto_df.to_csv('crypto_candle.csv')

	return crypto_df






def get_account_info():
	info = client.get_account()  # Getting account info
	return info

def get_balance_info(symbol):
	balance = client.get_asset_balance(asset=symbol)
	return balance


def display_graph():
	df = pd.read_csv('crypto_candle.csv')
	df=df.tail(10)

	fig = go.Figure(data=[go.Candlestick(x=df['dateTime'],
	                open=df['open'],
	                high=df['high'],
	                low=df['low'],
	                close=df['close'])])

	fig.show()	



