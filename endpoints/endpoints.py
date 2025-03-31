import requests
import os


class Endpoint:
    url = 'http://167.172.172.115:52355/'
    response = None
    for_all_memes = 'meme'
    body = {"name": "Daniil Katkov"}
    my_authorize = 'authorize'
    my_token = None
    headers = {"Authorization": ""}
    user = None

    base_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(base_dir, "creds.txt")

    def get_new_token(self):
        with open(self.token_path, 'w') as token_new:
            self.response = requests.post(f'{self.url}/{self.my_authorize}', json=self.body)
            self.my_token = self.response.json()['token']
            token_new.write(self.my_token)
            self.headers["Authorization"] = self.my_token
            self.user = self.response.json()["user"]
            print(self.headers["Authorization"])
            return self.response

    def check_token(self):
        with open(self.token_path, 'r') as token_check:
            token = token_check.read().strip()
            self.response = requests.get(f'{self.url}/{self.my_authorize}/{token}')
            if self.response.status_code == 200:
                self.headers["Authorization"] = token
                print(self.headers["Authorization"])
                return self.response
            else:
                self.get_new_token()

    def check_status_code(self):
        assert self.response.status_code == 200, 'Not 200'

    def check_user_name(self):
        assert self.user == self.body["name"], 'Another user'
