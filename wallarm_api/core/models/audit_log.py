from datetime import datetime
from typing import List, Union

from pydantic import BaseModel

from wallarm_api.core.enums.action import Action
from wallarm_api.core.enums.object_type import ObjectType


class Diff(BaseModel):
    before: dict = None
    after: dict = None


class Log(BaseModel):
    action: Action
    diff: Diff
    entity: dict = None
    subject_id: Union[int, str]
    subject_clientid: int
    object_type: ObjectType
    object_userid: int
    object_clientid: int
    time: datetime
    realid: str


class Logs(BaseModel):
    objects: List[Log]
    continuation: str = None
