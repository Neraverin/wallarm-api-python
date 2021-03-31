from pydantic import BaseModel


class GraphSummaryMonthly(BaseModel):
    requests_count: int
    attacks_count: int
    blocked_attacks_count: int
