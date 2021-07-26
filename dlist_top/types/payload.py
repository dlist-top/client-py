from types import SimpleNamespace
from typing import Any
from enum import Enum

class GatewayOP(Enum):
    HELLO = 1
    IDENTIFY = 2
    READY = 3
    DISCONNECT = 4
    EVENT = 5

class GatewayPayload(SimpleNamespace):
    op: GatewayOP
    data: Any
    event: str

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.op = GatewayOP(kwargs['op'])