from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.audit_log import Logs


class AuditLogApi(BaseApi):
    def get_log(self, filters, limit=20):
        url = '/v1/audit_log'
        body = {'limit': limit, 'filter': filters}
        response = self.client.post(url, json=body)
        return Logs(**response['body'])
