# -*- coding: utf-8 -*-
import websocket
import gzip
import json
import sys

if "__main__" == __name__:
	ws = None

	# Socket Connection
	try:
		ws = websocket.create_connection("wss://api.huobipro.com/ws")
	except:
		print("Failed to Create Connection")
		sys.exit()

	# Candlestick Data
	req_dict = {
		"sub": "market.ethusdt.kline.1min",
		"id": "client_area : Candlestick Data"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Subscribe Market Depth
	req_dict = {
		"sub": "market.ethbtc.depth.step0",
		"id": "client_area : Subscribe Market Depth"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Receive
	while True:
		rcv_json = gzip.decompress(ws.recv()).decode('utf-8')
		rcv_dict = json.loads(rcv_json)

		if "ping" in rcv_dict:
			req_dict = {"pong": rcv_dict["ping"]}
			req_json = json.dumps(req_dict)
			ws.send(req_json)

		print(rcv_dict)
