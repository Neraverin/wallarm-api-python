import os

from wallarm_api import WallarmAPI


def get_env():
    api_UUID = os.environ.get('WALLARM_UUID')
    api_secret = os.environ.get('WALLARM_SECRET')
    return api_UUID, api_secret


if __name__ == '__main__':
    api_UUID, api_secret = get_env()
    api = WallarmAPI(api_UUID, api_secret)
    client_id = api.clients_api.get_client().id
    print(f'client_id = ', client_id)
    print(f'subscription = ', api.billing_api.get_subscription(client_id))
    print(f'dashboard_state = ', api.graph_api.get_dashboard_state(client_id))

