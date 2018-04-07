# -*- coding: utf-8 -*-
import websocket
import time
import json
import gzip

try:
	import thread
except ImportError:
	import _thread as thread


def run(ws):
	# Subscribe Market Depth
	req_dict = {"sub": "market.ethbtc.depth.step0", "id": "Subscribe Market Depth (ethbtc)"}
	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Subscribe Trade Detail
	req_dict = {"sub": "market.ethbtc.trade.detail", "id": "Subscribe Trade Detail (ethbtc)"}
	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Rcv Data 30 Seconds
	time.sleep(30)

	# Unsubscribe Market Depth
	req_dict = {"unsub": "market.ethbtc.depth.step0", "id": "Unsubscribe Market Depth (ethbtc)"}
	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Unsubscribe Trade Detail
	req_dict = {"unsub": "market.ethbtc.trade.detail", "id": "Unsubscribe Trade Detail (ethbtc)"}
	req_json = json.dumps(req_dict)
	ws.send(req_json)
	print(req_json)

	# Wait 5 Seconds
	time.sleep(5)

	# WebSocket Close
	ws.close()


def on_open(ws):
	thread.start_new_thread(run, (ws,))


def on_message(ws, rcv_data):
	rcv_dict = get_json(rcv_data)

	if "ping" in rcv_dict:
		req_dict = {"pong": rcv_dict["ping"]}
		req_json = json.dumps(req_dict)
		ws.send(req_json)
		print(req_json)

	print(rcv_dict)


def on_error(ws, msg):
	print(msg)


def on_close(ws):
	print("Closed !!")


def get_json(rcv_data):
	rcv_json = gzip.decompress(rcv_data).decode('utf-8')
	rcv_dict = json.loads(rcv_json)
	return rcv_dict


if __name__ == "__main__":
	websocket.enableTrace(False)
	url = "wss://api.huobi.pro/ws"
	ws_obj = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
	ws_obj.run_forever()

	print("FINISHED !!")
