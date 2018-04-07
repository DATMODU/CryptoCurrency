# -*- coding: utf-8 -*-
import websocket
import time
import json

try:
	import thread
except ImportError:
	import _thread as thread


def run(ws):
	# Subscribe Live Trades And Full level 2 orderBook
	req_dict = {"op": "subscribe", "args": ["trade:XBTUSD", "orderBookL2:XBTUSD"]}
	req_str = json.dumps(req_dict)
	ws.send(req_str)
	print(req_str)

	# Rcv Data 30 Seconds
	time.sleep(30)

	# Unsubscribe Live Trades And Full level 2 orderBook
	req_dict = {"op": "unsubscribe", "args": ["trade:XBTUSD", "orderBookL2:XBTUSD"]}
	req_str = json.dumps(req_dict)
	ws.send(req_str)
	print(req_str)

	# Rcv Data 30 Seconds
	time.sleep(5)

	# WebSocket Close
	ws.close()


def on_open(ws):
	thread.start_new_thread(run, (ws,))


def on_message(ws, rcv_json):
	rcv_dict = json.loads(rcv_json)
	print(rcv_dict)


def on_error(ws, msg):
	print(msg)


def on_close(ws):
	print("Closed !!")


if __name__ == "__main__":
	websocket.enableTrace(False)
	url = "wss://www.bitmex.com/realtime"
	ws_obj = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
	ws_obj.run_forever()

	print("FINISHED !!")
