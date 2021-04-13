from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.hint import Hint

class HintsApi(BaseApi):
    def get_hint_details(self, limit=100, offset=0, **kwargs):
            """
            :hit_id: list of two values
            :**kwargs: filter
            :return: response
            """
            response_list = []
            url = '/v1/objects/hint'
            params = {"filter": self.make_filter(**kwargs), "limit": limit, 'offset': offset}
            response = self.client.post(url, json=params)
            for hint in response['body']:
                response_list.append(Hint(**hint))
            return response_list

    def get_lom_version(self, clienid):
        url = f'/v2/lom_version/{clienid}'
        response = self.client.get(url=url)
        return response
