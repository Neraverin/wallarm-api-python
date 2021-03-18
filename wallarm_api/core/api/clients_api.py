from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.client import Client


class ClientsApi(BaseApi):
    def create_client(self, params):
        url = '/v1/objects/client/create'
        response = self.client.post(url, json=params)
        return Client(**response['body'])

    def get_client(self, client_id=None, enabled=True):
        url = '/v1/objects/client'
        body = {'filter': {'enabled': enabled}, 'limit': 1000, 'offset': 0}
        if client_id:
            body['filter'].update({'id': client_id})
        response = self.client.post(url, json=body)
        if len(response['body']) > 0:
            return Client(**response['body'][0])
        else:
            return None

    def get_clients(self, enabled=True):
        url = '/v1/objects/client'
        body = {'filter': {'enabled': enabled}, 'limit': 1000, 'offset': 0}
        response = self.client.post(url, json=body)
        if len(response['body']) > 0:
            client_list = [Client(**client) for client in response['body']]
            return client_list
        else:
            return None

    def update_client(self, client_id, params):
        url = '/v1/objects/client/update'
        body = {'filter': {'id': client_id}, 'fields': params}
        return self.client.post(url, json=body)

    def enable_client(self, clientid=None):
        url = "/v1/objects/client/enabling"
        params = {"clientid": clientid}
        response = self.client.post(url=url, json=params)
        return response

    def disable_client(self, clientid=None):
        url = "/v1/objects/client/disabling"
        params = {"clientid": clientid}
        response = self.client.post(url=url, json=params)
        return response
