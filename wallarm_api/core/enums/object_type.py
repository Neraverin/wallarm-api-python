from enum import Enum


class ObjectType(Enum):
    CLIENT = 'client'
    USER = 'user'
    SUBNETORIP = 'subnetorip'
    MFA = 'mfa'
    POOL = 'pool'
    INTEGRATION = 'integration'
    NODE = 'node'
    GROUPED_HINT = 'grouped_hint'
    ATTACK = 'attack'
    TRIGGER = 'triggers.trigger'
