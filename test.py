import os

from wallarm_api import WallarmAPI


def get_env():
    uuid = os.environ.get('WALLARM_UUID')
    secret = os.environ.get('WALLARM_SECRET')
    return uuid, secret


if __name__ == '__main__':
    api_UUID, api_secret = get_env()
    api = WallarmAPI(api_UUID, api_secret)
    client = api.clients_api.get_client()

    requests_count = 0
    clients = api.clients_api.get_clients()
    for client in clients:
        subscriptions = api.billing_api.get_subscription(client.id)
        for subscription in subscriptions:
            if subscription.type == 'trial' or subscription.state != 'active':
                continue

            dates = [[2021, 3]]
            for year, month in dates:
                stats = api.graph_api.get_requests_summary_monthly(client.id, year, month)
                if stats.blocked_attacks_count > 0:
                    requests_count += stats.requests_count

            break
    print('clients blocked_attacks_count', requests_count)
