#!/usr/bin/env python

import asyncio
import websockets
import json
from time import sleep

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")

async def test2(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Here is fun!")
        greeting = await websocket.recv()
        greeting = json.loads(greeting)
        print("greeting " + greeting['desc'])

async def longwait(uri):
    async with websockets.connect(uri) as ws:
        while True:
            # going to have to use if statements and JSON objects to determine what kind of event because I can't make custom events with this client library ugh
            sleep(2)
            await ws.send("Hello world!")
            greeting = await ws.recv()
            greeting = json.loads(greeting)
            print("greeting " + greeting['desc'])
        print("Outside the loop")

# asyncio.get_event_loop().run_until_complete(
#     hello('ws://socketio-tutorial-dgoodman.c9users.io:80'))
# asyncio.get_event_loop().run_until_complete(
#     test2('ws://socketio-tutorial-dgoodman.c9users.io:80')
# )
# So since this is async now I think we might just make one master connection and have the events triggered inside
asyncio.get_event_loop().run_until_complete(
    longwait('ws://socketio-tutorial-dgoodman.c9users.io:80')
)
print("done!")
