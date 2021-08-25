from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.node import Node


class NodeApi(BaseApi):
    def get_nodes(self, params):
        url = f'/v2/node'
        response = self.client.get(url, params=params)
        node_list = [Node(**node) for node in response["body"]]
        return node_list

    def get_instance_nodes(self, params={}):
        params.update({'filter[type]': 'node_instance'})
        instance_nodes = self.get_nodes(params=params)
        return instance_nodes
