import os

from wallarm_api import WallarmAPI


def get_env():
    api_UUID = os.environ.get('WALLARM_UUID')
    api_secret = os.environ.get('WALLARM_SECRET')
    api_host = os.environ.get('WALLARM_API', 'api.wallarm.com')
    return api_UUID, api_secret, api_host


if __name__ == '__main__':
    api_UUID, api_secret, api_host = get_env()
    api = WallarmAPI(api_UUID, api_secret, api_host)
    client_id = api.client_id
    print(f'client_id = ', client_id)
