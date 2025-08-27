import allure
import requests
import os

from endpoints.endpoints import Endpoint

class Token(Endpoint):
    body = {"name": "Daniil Katkov"}
    my_authorize = 'authorize'

    base_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(base_dir, "correct_creds.txt")

    @allure.step('Get new token')
    def get_new_token(self):
        with open(self.token_path, 'w') as token_new:
            self.response = requests.post(f'{self.url}/{self.my_authorize}', json=self.body)
            self.my_token = self.response.json()['token']
            token_new.write(self.my_token)
            self.headers["Authorization"] = self.my_token
            self.user = self.response.json()["user"]
            return self.response

    @allure.step('Check token life')
    def correct_token(self):
        with open(self.token_path, 'r') as token_check:
            token = token_check.read().strip()
            self.response = requests.get(f'{self.url}/{self.my_authorize}/{token}')
            if self.response.status_code == 200:
                self.headers["Authorization"] = token
            else:
                self.get_new_token()
            return self.response.text

    @allure.step('Check token with incorrect data')
    def incorrect_token(self):
        with open(self.token_path, 'r') as token_check:
            token = token_check.read().strip()[::-1]
            self.response = requests.get(f'{self.url}/{self.my_authorize}/{token}')
            return self.response

    @allure.step('Check equal text')
    def check_text(self):
        assert self.response.text == f'Token is alive. Username is {self.body["name"]}', f'Not {self.body["name"]}'

    @allure.step('Check equal user name')
    def check_user_name(self):
        assert self.user == self.body["name"], 'Another user'

    @allure.step('Check impossible getting memes without token')
    def no_token_for_get_memes(self, new_meme=None):
        new_meme = new_meme if new_meme else ""
        if new_meme:
            self.response = requests.get(f'{self.url}/{self.for_all_memes}/{new_meme}')
        else:
            self.response = requests.get(f'{self.url}/{self.for_all_memes}')
        return self.response.status_code

    @allure.step('Check impossible getting memes with incorrect token')
    def incorrect_token_for_get_memes(self, new_meme=None):
        new_meme = new_meme if new_meme else ""
        if new_meme:
            self.response = requests.get(f'{self.url}/{self.for_all_memes}/{new_meme}',
                                         headers=self.incorrect_headers)
        else:
            self.response = requests.get(f'{self.url}/{self.for_all_memes}', headers=self.incorrect_headers)
        return self.response.status_code

    @allure.step('Check impossible getting memes with empty token')
    def empty_token_for_get_memes(self, new_meme=None):
        new_meme = new_meme if new_meme else ""
        if new_meme:
            self.response = requests.get(f'{self.url}/{self.for_all_memes}/{new_meme}',
                                         headers=self.empty_headers)
        else:
            self.response = requests.get(f'{self.url}/{self.for_all_memes}', headers=self.empty_headers)
        return self.response.status_code
