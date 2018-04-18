#!/usr/bin/env python

import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")

async def test2(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Here is fun!")
        greeting = await websocket.recv()
        print("greeting " + greeting)

asyncio.get_event_loop().run_until_complete(
    hello('ws://socketio-tutorial-dgoodman.c9users.io:80'))
asyncio.get_event_loop().run_until_complete(
    test2('ws://socketio-tutorial-dgoodman.c9users.io:80')
)
