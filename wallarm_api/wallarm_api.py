import requests

from wallarm_api.core.api.clients_api import ClientsApi


class WallarmAPI:

    def __init__(self, uuid='', secret='', api='https://api.wallarm.com'):
        self.__uuid = uuid
        self.__secret = secret
        self.__api = api
        self.clients_api = ClientsApi(uuid, secret, host=api)
