import asyncio  #permite rodar em tempo real
import websockets  # conecta com o servidor
import ssl
import json
from json import dumps as json_dumps

URL = "wss://kxuhnbmureteruqbiubi.supabase.co/realtime/v1/websocket?apikey=sb_publishable__g31vlBJkb-juSG7ilze1A_9dFr-Z3N&vsn=2.0.0"

async def listen(on_message):
    ssl_context = ssl._create_unverified_context()

    async with websockets.connect(URL, ssl=ssl_context) as ws:
        join_message = {
            "topic": "realtime:coding-presence",
            "event": "phx_join", 
            "payload": {
                "config": {
                    "broadcast": {
                        "ack" : False,
                        "self": False
                    }
                }
            },
            "ref": "1"
        }

        await ws.send(json_dumps(join_message))

        while True:
            message = await ws.recv() #recebe a mensagem
            on_message(message)

