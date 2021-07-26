import asyncio
import websockets
import json
import logging
from pyee import BaseEventEmitter

from .const import gateway_url
from .types import Entity, GatewayPayload, GatewayOP, event_classes

class Client(BaseEventEmitter):
    entity: Entity

    def __init__(self, token: str):
        self.token = token
        self.logger = logging.getLogger('dlist_client')
        self.logger.setLevel(logging.DEBUG)

    def connect(self):
        asyncio.get_event_loop().run_until_complete(self._connect())

    async def _connect(self):
        async with websockets.connect(gateway_url) as ws:
            while True:
                msg = await ws.recv()
                payload = GatewayPayload(**json.loads(msg))

                if payload.op == GatewayOP.HELLO:
                    await ws.send(json.dumps({
                        'op': GatewayOP.IDENTIFY.value,
                        'data': {
                            'token': self.token
                        }
                    }))

                elif payload.op == GatewayOP.READY:
                    self.entity = Entity(**payload.data)
                    self.logger.info(f'[READY] connected to entity: {self.entity}')

                elif payload.op == GatewayOP.EVENT:
                    cls = event_classes[payload.event]
                    data = cls(**payload.data)
                    self.emit(payload.event.lower(), data)

                else:
                    print(payload)
                    
                
                
