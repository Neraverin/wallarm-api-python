from pydantic import BaseModel


class Integration(BaseModel):
    id: int
    active: bool
    name: str
    type: str
    created_at: int
    created_by: str
    events: list
    system_active: bool
    resource_type: str
