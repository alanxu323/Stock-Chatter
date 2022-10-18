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
	elif msg == "小狐狸":
		response = "深度睿智！"
	elif msg == "主人宝贝":
		response = "最聪明的人，拍拍聪明可爱大脑袋"
	elif msg == "世界上最可爱的人是谁":
		response = "是Guniu呜们!"
	
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

#Account ID(TWILIO_ACCOUNT, TWILIO_TOKEN)
#AC62ff9d67e3160c8fcb96f6a993aa3391
#Token
#2c95e1bd47890942c2aec2264ceb92cc
