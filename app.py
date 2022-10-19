from flask import Flask
from flask import request
from twilio.rest import Client
import os
from marketstack import get_stock_price
app = Flask(__name__)

sid = os.environ.get('TWILIO_ACCOUNT')
t_token = os.environ.get('TWILIO_TOKEN')
client = Client(sid,t_token)
NUMBER = 'whatsapp:+14155238886'

def process_msg(msg):
	response = ""
	if msg.lower() == "Hi".lower():
		response = "Welcome to the stock market bot!"
		response += "Type sym:<stock_symbol> to know the price of the stock"
	elif 'sym:' in msg:
		data = msg.split(":")
		stock_symbol = data[1]
		stock_price = get_stock_price(stock_symbol)
		response = stock_price
	
	else:
		response = "Please type hi to get started"
	return response

def send_msg(msg,recipient):
	client.messages.create(
		from_ = NUMBER,
		body = msg,
		to = recipient
	)

@app.route("/webhook", methods = ["POST"])
def webhook():
	f = request.form
	msg = f['Body']
	sender = f['From']
	response = process_msg(msg)
	send_msg(response, sender)
	return "OK", 200
