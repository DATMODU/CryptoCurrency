# -*- coding: utf-8 -*-
import websocket
import json
import sys

if "__main__" == __name__:
	ws = None

	try:
		ws = websocket.create_connection("wss://real.okcoin.com:10440/websocket")
	except:
		print("Failed to Create Connection")
		sys.exit()

	# Ticker
	req_dict = {
		"event": "addChannel",
		"channel": "ok_sub_spot_btc_usd_ticker"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Depth
	req_dict = {
		"event": "addChannel",
		"channel": "ok_sub_spot_btc_usd_depth"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Receive
	while True:
		rcv_json = ws.recv()
		rcv_dict = json.loads(rcv_json)
		print(rcv_dict)
