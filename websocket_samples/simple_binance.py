# -*- coding: utf-8 -*-
import websocket
import time
import json
import ssl

try:
	import thread
except ImportError:
	import _thread as thread


def run(ws):
	# Rcv Data 30 Seconds
	time.sleep(30)

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
	url = "wss://stream.binance.com:9443/stream?streams=btcusdt@trade/btcusdt@depth"
	ws_obj = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
	ws_obj.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

	print("FINISHED !!")
