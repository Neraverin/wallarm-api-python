from datetime import datetime
from typing import List

from pydantic import BaseModel

from wallarm_api.core.enums.component import Component
from wallarm_api.core.enums.language import Language
from wallarm_api.core.enums.role import Role
from typing import Optional

class LoginHistory(BaseModel):
    time: datetime
    ip: str

class User(BaseModel):
    id: int
    email: str
    password: str = None
    clientid: int
    uuid: str
    permissions: List[str]
    actual_permissions: List[str]
    mfa_enabled: bool
    create_by: datetime = None
    create_at: datetime = None
    create_from: str = None
    enabled: bool
    validated: bool
    username: str
    realname: str = None
    phone: str = None
    password_changed: int
    login_history: List[LoginHistory] = []
    timezone: str
    results_per_page: int
    default_pool: str
    default_poolid: int = None
    search_templates: dict = None
    # notifications: {}
    components: List[Component]
    language: Language
    last_login_time: datetime = None
    date_format: str
    time_format: str
    job_title: str = None
    frontend_url: str = None
    available_authentications: List[str]
    secret: Optional[str]


class Users(BaseModel):
    users: List[User] = []
