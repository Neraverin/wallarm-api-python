import time
import datetime


from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.dashboard import DashboardState
from wallarm_api.core.models.graph_data import GraphSummaryMonthly


class GraphApi(BaseApi):
    def get_attacks_stats(self, client_id=None, start_time=None, end_time=None):
        url = f'/v2/graph_data/attacks_stats/total/client/{client_id}'
        if start_time is None or end_time is None:
            start_time = (int(time.time()) - 86400)
            end_time = int(time.time())
        params = {
            "request_categories": ["attacks"], "fields": ["countries", "datacenters", "tors"], "start_time": start_time,
            "end_time": end_time
        }
        response = self.client.post(url=url, json=params)
        return response

    def get_rps_stats(self, client_id=None, start_time=None, end_time=None, points_count=1):
        url = f'/v2/graph_data/rps/client/{client_id}'
        if start_time is None or end_time is None:
            start_time = (int(time.time()) - 86400)
            end_time = int(time.time())
        params = {
            "interpolation": "linear", "start_time": start_time, "end_time": end_time, "points_count": points_count
        }
        response = self.client.post(url=url, json=params)
        return response

    def get_targets_stats(self, client_id=None, start_time=None, end_time=None):
        url = f'/v2/graph_data/targets/total/client/{client_id}'
        if start_time is None or end_time is None:
            start_time = (int(time.time()) - 86400)
            end_time = int(time.time())
        params = {"start_time": start_time, "end_time": end_time}
        response = self.client.post(url=url, json=params)
        return response

    def get_testrun_stats(self, client_id=None, start_time=None, end_time=None, points_count=17):
        if start_time is None or end_time is None:
            start_time = (int(time.time()) - 86400)
            end_time = int(time.time())
        url = f'/v1/graph_data/testrun?start_time={start_time}&end_time={end_time}' \
              f'&points_count={points_count}&clientid={client_id}'
        response = self.client.get(url=url)
        return response

    def get_blacklist_stats(self, client_id=None, start_time=None, end_time=None, points_count=17):
        url = f'/v2/graph_data/blacklist_size/client/{client_id}/full'
        if start_time is None or end_time is None:
            start_time = (int(time.time()) - 86400)
            end_time = int(time.time())
        params = {"start_time": start_time, "end_time": end_time, "points_count": points_count}
        response = self.client.post(url=url, json=params)
        return response

    def get_baseline_stats(self, client_id=None, start_time=None, end_time=None, points_count=32):
        if start_time is None or end_time is None:
            start_time = (int(time.time()) - 86400)
            end_time = int(time.time())
        url = f'/v1/graph_data/baseline?start_time={start_time}&end_time={end_time}' \
              f'&points_count={points_count}&clientid={client_id}'
        response = self.client.get(url=url)
        return response

    def get_dashboard_state(self, clientid):
        url = f'/v2/dashboard_state/{clientid}'
        response = self.client.get(url=url)
        return DashboardState(**response['body']['object'])

    def get_requests_summary_monthly(self, client_id=None, year=None, month=None):
        url = f'/v2/graph_data/summary/monthly/total/client/{client_id}'
        if year is None or month is None:
            now = datetime.datetime.now()
            year = now.year
            month = now.month
        params = {
            "year": year, "month": month,
        }
        response = self.client.post(url=url, json=params)
        return GraphSummaryMonthly(**response['body'])
