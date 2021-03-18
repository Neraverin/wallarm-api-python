from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.billing import *
from datetime import datetime, timedelta


class BillingApi(BaseApi):
    def create_feature(self, name):
        url = "/v1/billing/features"
        data = {"feature": {"slug": name}}
        response = self.client.post(url, json=data)
        return Feature(**response)

    def create_plan(self, params):
        url = "/v1/billing/plans"
        response = self.client.post(url, json=params)
        return Plan(**response)

    def get_plans(self):
        url = "/v1/billing/plans"
        response = self.client.get(url)
        response_list = []
        for plan in response:
            response_list.append(PlanElement(**plan))
        return response_list

    def create_binding(self, plan_id, feature_id, settings=None):
        settings = settings or {"enabled": {"value": True}}
        url = "/v1/billing/plans/%s/bindings" % plan_id
        params = {"binding": {"feature_id": feature_id, "settings": settings}}
        response = self.client.post(url=url, json=params)
        return Binding(**response)

    def subscribe(self, client_id, plan_id, subscription_type, date_beg=None, date_end=None):
        url = "/v1/clients/%s/billing/subscriptions" % client_id
        params = {
            "subscription": {
                "plan_id": plan_id,
                "type": subscription_type,
                "start_on": date_beg.strftime("%Y-%m-%d"),
                "finish_on": date_end.strftime("%Y-%m-%d"),
            }
        }
        response = self.client.post(url, json=params)
        return Subscription(**response)

    def update_subscription(self, client_id, subscription_id, plan_id, subscription_type, date_beg=None, date_end=None):
        url = "/v1/clients/%s/billing/subscriptions/%s" % (client_id, subscription_id)
        params = {
            "subscription": {
                "plan_id": plan_id,
                "type": subscription_type,
                "start_on": date_beg.strftime("%Y-%m-%d"),
                "finish_on": date_end.strftime("%Y-%m-%d"),
            }
        }
        response = self.client.put(url, json=params)
        return Subscription(**response)

    def extend_trial_by_jwt(self, jwt):
        url = "/v1/billing/subscriptions/trials"
        params = {"jwt": jwt}
        response = self.client.post(url, json=params)
        return Subscription(**response)

    def extend_trial_by_user(self, client_id):
        url = "/v1/clients/%s/billing/subscriptions/trials" % client_id
        response = self.client.post(url, json={})
        return Subscription(**response)

    def extend_trial_by_superadmin(self, client_id):
        url = "/v1/clients/%s/billing/admin/subscriptions/trials" % client_id
        response = self.client.post(url, json={})
        return Subscription(**response)

    def subscribe_annual(self, client_id, plan_id):
        date_end = datetime.today().date() + timedelta(days=365)
        date_beg = datetime.today().date()
        return self.subscribe(client_id, plan_id, "annual", date_beg, date_end)

    def get_subscription(self, client_id):
        url = "/v1/clients/%s/billing/subscriptions" % client_id
        response = self.client.get(url)
        result = []
        for subscr in response:
            result.append(Subscription(**subscr))
        return result

    def update_partner_settings(self, partner_id, settings):
        url = "/v1/partners/%s/billing/settings" % partner_id
        params = {
            "partner_setting": settings
        }
        response = self.client.post(url, json=params)
        return PartnerSettings(**response)

    def delete_partner_settings(self, partner_id):
        url = "/v1/partners/%s/billing/settings" % partner_id
        response = self.client.delete(url, json={})
        return response
