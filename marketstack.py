import os
import requests
import json

api_key = os.environ.get("mk")
base_url = 'http://api.marketstack.com/v1/tickers/'
params = {
  'access_key': api_key
}
def get_stock_price(stock_symbol):
	params = {
		'access_key': api_key
	}
	
	api_result = requests.get('http://api.marketstack.com/v1/tickers/aapl/intraday/latest', params)
	print(api_result)
	
	json_result = json.loads(api_result.text)

	return{"highest": json_result["high"],
		"lowest": json_result["low"],
		"close": json_result["close"]}
