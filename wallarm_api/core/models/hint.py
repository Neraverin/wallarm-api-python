from pydantic import BaseModel


class Hint(BaseModel):
    id: int
    actionid: int
    clientid: int
    action: list
    create_time: int
    create_userid: int
    validated: bool
    system: bool
    regex_id: str = None
    updated_at: int
    type: str
    point: list = None
    counter: str = None
    comment: str = None
