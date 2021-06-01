from weakref import WeakValueDictionary
from wallarm_api.core.api.attacks_api import AttacksApi
from wallarm_api.core.api.clients_api import ClientsApi
from wallarm_api.core.api.billing_api import BillingApi
from wallarm_api.core.api.graph_api import GraphApi
from wallarm_api.core.api.hints_api import HintsApi
from wallarm_api.core.api.users_api import UsersApi
from wallarm_api.core.api.vulnerabilities_api import VulnerabilitiesApi
from wallarm_api.core.api.integrations_api import IntegrationsApi

class Singleton(type):
    _instances = WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class WallarmAPI(metaclass=Singleton):

    def __init__(self, uuid: str, secret: str, api: str):
        self.__uuid = uuid
        self.__secret = secret
        self.__api = api
        self.clients_api = ClientsApi(uuid, secret, host=api)
        self.billing_api = BillingApi(uuid, secret, host=api)
        self.graph_api = GraphApi(uuid, secret, host=api)
        self.hints_api = HintsApi(uuid, secret, host=api)
        self.users_api = UsersApi(uuid, secret, host=api)
        self.vulns_api = VulnerabilitiesApi(uuid, secret, host=api)
        self.integrations_api = IntegrationsApi(uuid, secret, host=api)
        self.attacks_api = AttacksApi(uuid, secret, host=api)
