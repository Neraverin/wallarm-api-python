from datetime import datetime
from typing import Optional, Dict

from pydantic import BaseModel


class Node(BaseModel):
    clientid: int
    create_from: str = None
    create_time: datetime
    enabled: bool
    hostname: str
    id: int
    ip: str = None
    last_activity: datetime = None
    last_analytic: datetime = None
    lom_version: int = None
    protondb_version: int = None
    requests_amount: Optional[int]
    type: str
    token: str = None
    active: bool
    active_instance_count: int = None
    instance_count: int = None
    secret: Optional[str]
    uuid: str
    node_env_params: Dict
