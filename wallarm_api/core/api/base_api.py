from wallarm_api.core.clients.bare_http_client import BareHttpClient
from wallarm_api.core.clients.response_handler import DefaultJsonContentHandler, OKStatusHandler, NOKStatusHandler, \
    ErrorStatusHandler


class BaseApi:
    def __init__(self, uuid, secret, host, *args, **kwargs):
        self.client = BareHttpClient(
            host,
            default_headers={
                "X-WallarmAPI-UUID": uuid,
                "X-WallarmAPI-Secret": secret
            }
        )
        self.client.add_content_handler(DefaultJsonContentHandler())
        self.client.add_errors_handler(OKStatusHandler())
        self.client.add_errors_handler(NOKStatusHandler())
        self.client.add_errors_handler(ErrorStatusHandler())

    @staticmethod
    def make_filter(**kwargs):
        attack_filter_json = {}
        if 'non_args' in kwargs.keys():
            attack_filter_json.update(kwargs['non_args'])
            kwargs.pop('non_args')
        for i in kwargs:
            if i in ('attackid', 'hitid'):
                if type(kwargs[i]) == str:
                    value = list(kwargs[i].split(':'))
                else:
                    value = kwargs[i]
                attack_filter_json[i] = value
            else:
                attack_filter_json[i] = kwargs[i]
        return attack_filter_json
