from enum import Enum


class Action(Enum):
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'
    MARK_FALSE = "mark_false"