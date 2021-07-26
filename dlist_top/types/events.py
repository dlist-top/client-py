from types import SimpleNamespace
from typing import Any
from datetime import datetime
from .entity import EntityType

class VoteData(SimpleNamespace):
    authorID: str
    entityType: EntityType
    entityID: str
    date: datetime
    totalVotes: int
    userVotes: int

    def __init__(self, entityType, date, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.entityType = EntityType(entityType)
        self.date = datetime.utcfromtimestamp(date)

class RateData(SimpleNamespace):
    authorID: str
    entityType: EntityType
    entityID: str
    rating: int
    details: str
    date: datetime

    def __init__(self, entityType, date, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.entityType = EntityType(entityType)
        self.date = datetime.utcfromtimestamp(date)

event_classes = {
    'VOTE': VoteData,
    'RATE': RateData
}