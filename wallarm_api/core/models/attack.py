from pydantic import BaseModel


class Attack(BaseModel):
    id: list
    attackid: str
    clientid: int
    domain: str = None
    method: str
    parameter: str
    path: str
    type: str
    first_time: int
    last_time: int
    hits: int
    anomality: list = None
    ip_count: int
    ip_top: list
    datacenter: list
    tor: str = None
    country_count: int
    country_top: list
    statuscodes: list
    vulnid: int = None
    threat: int
    target: str
    experimental: str = None
    recheck_status: str = None
    recheck_time: int = None
    vectors_count: int
    block_status: str = None
    state: str = None
    sid: list
    point: list
    vulns: list
    hits_count_by_filter: int
    ip_count_by_filter: int
    vectors_count_by_filter: int = None
    statuscodes_by_filter: list = None
