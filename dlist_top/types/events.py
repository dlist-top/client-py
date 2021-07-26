from types import SimpleNamespace
from typing import Any
from .entity import EntityType

class VoteData(SimpleNamespace):
    authorID: str
    entityType: EntityType
    entityID: str
    date: int
    totalVotes: int
    userVotes: int

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.entityType = EntityType(kwargs['entityType'])

class RateData(SimpleNamespace):
    authorID: str
    entityType: EntityType
    entityID: str
    rating: int
    details: str
    date: int

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.entityType = EntityType(kwargs['entityType'])

event_classes = {
    'VOTE': VoteData,
    'RATE': RateData
}