import asyncio
import websockets
import json
import logging
from pyee import BaseEventEmitter

from .const import gateway_url
from .types import Entity, GatewayPayload, GatewayOP, event_classes

class Client(BaseEventEmitter):
    entity: Entity

    def __init__(self, token: str, log_level: int = logging.INFO):
        self.token = token
        self.logger = logging.getLogger('dlist_top')
        self.logger.setLevel(log_level)

    def connect(self):
        asyncio.get_event_loop().run_until_complete(self._connect())

    async def _connect(self):
        async with websockets.connect(gateway_url) as ws:
            while True:
                msg = await ws.recv()
                payload = GatewayPayload(**json.loads(msg))

                if payload.op == GatewayOP.HELLO:
                    self.logger.debug(f'Connected. Message: "{payload.data}"')
                    await ws.send(json.dumps({
                        'op': GatewayOP.IDENTIFY.value,
                        'data': {
                            'token': self.token
                        }
                    }))
                    self.logger.debug('Identify packet sent')

                elif payload.op == GatewayOP.READY:
                    self.entity = Entity(**payload.data)
                    self.logger.info(f'Ready. Connected to: {self.entity}')
                    self.emit('ready', self.entity)

                elif payload.op == GatewayOP.EVENT:
                    if payload.event not in event_classes:
                        self.logger.debug(f'Unsupported event: {payload.event}')
                        break

                    cls = event_classes[payload.event]
                    data = cls(**payload.data)
                    self.logger.debug(f'Event received: {payload.event}')
                    self.emit(payload.event.lower(), data)

                else:
                    self.logger.debug(f'Unsupported OP: {payload.op}')
                