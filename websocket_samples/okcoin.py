# -*- coding: utf-8 -*-
import websocket
import json
import sys

if "__main__" == __name__:

	# Socket Connection
	ws = websocket.WebSocket()
	try:
		ws.connect("wss://real.okcoin.com:10440/websocket")
	except:
		print("Failed to Create Connection")
		sys.exit()

	# Add Ticker Channel
	req_dict = {
		"event": "addChannel",
		"channel": "ok_sub_spot_btc_usd_ticker"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Add Depth Channel
	req_dict = {
		"event": "addChannel",
		"channel": "ok_sub_spot_btc_usd_depth"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Receive 50 times
	unsub_cnt = 0
	while 50 > unsub_cnt:
		rcv_json = ws.recv()
		rcv_dict = json.loads(rcv_json)
		print(rcv_dict)

		unsub_cnt = unsub_cnt + 1

	# Remove Ticker Channel
	req_dict = {
		"event": "removeChannel",
		"channel": "ok_sub_spot_btc_usd_ticker"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Remove Depth Channel
	req_dict = {
		"event": "removeChannel",
		"channel": "ok_sub_spot_btc_usd_depth"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# WebSocket Close
	ws.close()
	print("WebSocket Closed")
