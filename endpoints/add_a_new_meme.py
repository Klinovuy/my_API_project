from endpoints.endpoints import Endpoint
from endpoints.token import Token
from endpoints.test_data import payload
import requests
import allure


class AddMeme(Token, Endpoint):
    object_id = None
    text = None
    url_meme = None
    tags = None
    info = None
    bad_object_id = None

    @allure.step('Check adding a correct meme')
    def add_a_correct_meme(self):
        self.correct_token()
        self.response = requests.post(f'{self.url}/{self.for_all_memes}', json=payload, headers=self.headers)
        if self.response.status_code == 200:
            self.object_id = self.response.json()["id"]
            self.text = self.response.json()["text"]
            self.url_meme = self.response.json()["url"]
            self.tags = self.response.json()["tags"]
            self.info = self.response.json()["info"]
        return self.response

    @allure.step('Check equal text')
    def check_body_text(self):
        assert self.text == payload["text"]

    @allure.step('Check equal url')
    def check_url(self):
        assert self.url_meme == payload["url"]

    @allure.step('Check equal tags')
    def check_tags(self):
        assert self.tags == payload["tags"]

    @allure.step('Check equal info')
    def check_info(self):
        assert self.info == payload["info"]

    @allure.step('Check impossible adding an incorrect meme')
    def add_an_incorrect_meme(self, incorrect_data):
        self.correct_token()
        self.response = requests.post(f'{self.url}/{self.for_all_memes}', json=incorrect_data, headers=self.headers)
        if self.response.status_code == 200:
            self.bad_object_id = self.response.json()["id"]
            requests.delete(f'{self.url}/{self.for_all_memes}/{self.bad_object_id}', headers=self.headers)
            print("Мем незапланированно был создан, но теперь удалён")
        return self.response.status_code

    @allure.step('Check impossible adding a new meme without token')
    def no_token_for_add_a_new_meme(self):
        self.response = requests.post(f'{self.url}/{self.for_all_memes}', json=payload)
        return self.response.status_code

    @allure.step('Check impossible adding a new meme with incorrect token')
    def incorrect_token_for_add_a_new_meme(self):
        self.response = requests.post(f'{self.url}/{self.for_all_memes}', json=payload,
                                      headers=self.incorrect_headers)
        return self.response.status_code

    @allure.step('Check impossible adding a new meme with empty token')
    def empty_token_for_add_a_new_meme(self):
        self.response = requests.post(f'{self.url}/{self.for_all_memes}', json=payload, headers=self.empty_headers)
        return self.response.status_code
