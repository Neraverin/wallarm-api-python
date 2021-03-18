from pydantic import BaseModel


class DashboardState(BaseModel):
    vulns: bool
    scope: bool
    nodes: bool
    traffic: bool
    attacks: bool
    nodes_active: int
    nodes_count: int
    testrun: bool
    requests_amount: int
