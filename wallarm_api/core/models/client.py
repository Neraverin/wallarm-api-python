from datetime import datetime
from typing import List

from pydantic import BaseModel

from wallarm_api.core.enums.component import Component
from wallarm_api.core.enums.language import Language


class Notification(BaseModel):
    email: list = []
    telegram: list = []
    slack: list = []
    splunk: list = []
    pager_duty: list = []


class Notifications(BaseModel):
    report_daily: Notification
    report_weekly: Notification
    report_monthly: Notification
    vuln: Notification
    scope: Notification = None
    system: Notification = None


class ScannerState(BaseModel):
    last_scan: str = None
    last_vuln: str = None
    last_vuln_check: str = None
    last_wapi: str = None


class Client(BaseModel):
    id: int
    name: str
    vuln_prefix: str
    components: List[Component]
    support_plan: str
    date_format: str
    mode: str
    blocking_type: str
    scanner_mode: str
    qrator_blacklists: bool
    notifications: Notifications
    scanner_cluster: str
    scanner_scope_cluster: str
    scanner_state: ScannerState
    language: Language
    attack_rechecker_mode: str
    vuln_rechecker_mode: str
    validated: bool
    enabled: bool
    create_at: datetime
    partnerid: int
    hidden_vulns: bool
    scanner_priority: str
    qrator_mode: str = None
    last_scan: str = None
    can_enable_blacklist: bool = None
    blacklist_disabled_at: datetime = None
    ngenixids: List[int] = []
    qratorids: List[int] = []
