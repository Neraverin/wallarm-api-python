from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.integration import Integration


class IntegrationsApi(BaseApi):
    def get_integrations(self, clientid):
        url = f'/v2/integration?clientid={clientid}'
        response = self.client.get(url=url)
        response_list = []
        for integration in response['body']['object']:
            response_list.append(Integration(**integration))
        return response_list
