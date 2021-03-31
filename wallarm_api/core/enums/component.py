from enum import Enum


class Component(Enum):
    WAF = 'waf'
    FAST = 'fast'
    license = 'license'
    nodedata = 'nodedata'
# TODO: remove this crutch for typos in the components
    lisence = 'lisence'
    closed = 'closed'
