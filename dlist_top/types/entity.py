from types import SimpleNamespace
from typing import Any
from enum import Enum

class EntityType(Enum):
    BOT = 'bots'
    SERVER = 'servers'

class Entity(SimpleNamespace):
    type: EntityType
    id: str
    name: str

    def __init__(self, type, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.type = EntityType(type)