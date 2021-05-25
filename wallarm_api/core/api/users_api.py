from wallarm_api.core.api.base_api import BaseApi
from wallarm_api.core.models.user import Users

class UsersApi(BaseApi):
    def get_users(self, params):
            url = '/v1/objects/user'
            response = self.client.post(url, json={'filter': params})
            try:
                users = Users(users=response['body'])
            except ValueError as err:
                print("Can't parce users model")
                print(err)
                return Users(users=[])
            else:
                return users