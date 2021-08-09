from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.trigger import Triggers

class TriggersApi(BaseApi):
    def get_triggers(self, clientid):
            url = f'/v2/clients/{clientid}/triggers?denormalize=true'
            response = self.client.get(url)
            triggers = Triggers(triggers=response['triggers'])
            return triggers
