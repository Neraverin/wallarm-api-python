from wallarm_api.core.api.clients_api import ClientsApi
from wallarm_api.core.api.billing_api import BillingApi
from wallarm_api.core.api.graph_api import GraphApi
from wallarm_api.core.api.hints_api import HintsApi
from wallarm_api.core.api.users_api import UsersApi
from wallarm_api.core.api.vulnerabilities_api import VulnerabilitiesApi


class WallarmAPI:

    def __init__(self, uuid='', secret='', api='https://api.wallarm.com'):
        self.__uuid = uuid
        self.__secret = secret
        self.__api = api
        self.clients_api = ClientsApi(uuid, secret, host=api)
        self.billing_api = BillingApi(uuid, secret, host=api)
        self.graph_api = GraphApi(uuid, secret, host=api)
        self.hints_api = HintsApi(uuid, secret, host=api)
        self.users_api = UsersApi(uuid, secret, host=api)
        self.vulns_api = VulnerabilitiesApi(uuid, secret, host=api)
