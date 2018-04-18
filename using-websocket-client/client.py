#!/usr/bin/python
import websocket
import thread
import time

def on_message(ws, message):
    print message + "hehheheheheheh!!!"

def on_error(ws, error):
    print error

def on_testT(ws, msg):
    print msg

def on_close(ws):
    print "### closed ###"
    # Attemp to reconnect with 2 seconds interval
    time.sleep(2)
    initiate()

def on_open(ws):
    print "### Initiating new websocket connection ###"
    def run(*args):
        for i in range(30000):
            # Sending message with 1 second intervall
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print "thread terminating..."
    thread.start_new_thread(run, ())

def initiate():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://167.99.14.231/",
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()

if __name__ == "__main__":
    initiate()
