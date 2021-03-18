import requests

from wallarm_api.core.api.clients_api import ClientsApi


class WallarmAPI:

    def __init__(self, uuid='', secret='', api='api.wallarm.com'):
        self.__uuid = uuid
        self.__secret = secret
        self.__api = api
        self.client_id = self.get_client_id(self)
        self.clients_api = ClientsApi(uuid, secret, host=api)

    @staticmethod
    def get_client_id(self):
        """The method to fetch a clientid for some queries"""

        url = f'https://{self.__api}/v1/objects/client'
        body = {"filter": {}}
        with requests.post(url, json=body,
                           headers={'X-WallarmAPI-UUID': self.__uuid,
                                    'X-WallarmAPI-Secret': self.__secret}) as response:
            if response.status_code not in [200, 201, 202, 204, 304]:
                raise NameError('invalid response')

        return response.json().get('body')[0].get('id')
