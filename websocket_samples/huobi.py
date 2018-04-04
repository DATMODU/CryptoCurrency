# -*- coding: utf-8 -*-
import websocket
import gzip
import json
import sys

if "__main__" == __name__:

	# WebSocket Connection
	ws = websocket.WebSocket()
	try:
		ws.connect("wss://api.huobipro.com/ws")
	except:
		print("Failed to Create Connection")
		sys.exit()

	# Subscribe Market Depth
	req_dict = {
		"sub": "market.ethbtc.depth.step0",
		"id": "Subscribe Market Depth (ethbtc)"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Subscribe Trade Detail
	req_dict = {
		"sub": "market.ethbtc.trade.detail",
		"id": "Subscribe Trade Detail (ethbtc)"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Receive 50 times
	unsub_cnt = 0
	while 50 > unsub_cnt:
		rcv_json = gzip.decompress(ws.recv()).decode('utf-8')
		rcv_dict = json.loads(rcv_json)

		print(rcv_dict)

		if "ping" in rcv_dict:
			req_dict = {"pong": rcv_dict["ping"]}
			req_json = json.dumps(req_dict)
			ws.send(req_json)

		unsub_cnt = unsub_cnt + 1

	# Unsubscribe Market Depth
	req_dict = {
		"unsub": "market.ethbtc.depth.step0",
		"id": "Unsubscribe Market Depth (ethbtc)"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Unsubscribe Trade Detail
	req_dict = {
		"unsub": "market.ethbtc.trade.detail",
		"id": "Unsubscribe Trade Detail (ethbtc)"
	}

	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# WebSocket Close
	ws.close()
	print("WebSocket Closed")
