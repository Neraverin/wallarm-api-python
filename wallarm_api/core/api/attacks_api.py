from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.attack import Attack

class AttacksApi(BaseApi):
    def get_attacks_by_filter(self, **kwargs):
            """
            :param non_args: dict for non values - !parameter, !state, etc
            :param kwargs: filter, look like this: clientid=132, path=pathgen[:-1], etc
            :return: response
            """
            response_list = []
            url = '/v1/objects/attack'
            params = {"filter": self.make_filter(**kwargs)}
            response = self.client.post(url, json=params)
            for attack in response['body']:
                response_list.append(Attack(**attack))
            return response_list