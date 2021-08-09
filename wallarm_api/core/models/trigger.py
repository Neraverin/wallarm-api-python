from datetime import datetime
from typing import List

from pydantic import BaseModel

class Filter(BaseModel):
    id: str
    operator: str
    type: str
    #values: List[str] = []

class Trigger(BaseModel):
    id: int
    name: str
    actions: List[dict]
    client_id: int
    comment: str = None
    created_at: datetime
    enabled: bool
    filters: List[Filter] = []
    template: dict
    template_id: str
    thresholds: List[dict] = []
    updated_at: datetime

class Triggers(BaseModel):
    triggers: List[Trigger] = []