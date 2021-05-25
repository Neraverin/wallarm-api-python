from typing import Dict


from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.vulnerability import Vulnerability, VulnTemplate


class VulnerabilitiesApi(BaseApi):

    def get_vulns_by_filter(self, limit=100, offset=0, **kwargs):
        """
        :limit: int, by default 100
        :**kwargs: filter
        :return: response
        """
        url = '/v1/objects/vuln'
        params = {"filter": self.make_filter(
            **kwargs), "limit": limit, 'offset': offset}
        response = self.client.post(url, json=params)
        vulnerabilities = [Vulnerability(**vuln) for vuln in response["body"]]
        return vulnerabilities
