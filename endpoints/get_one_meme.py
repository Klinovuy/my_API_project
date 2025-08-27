import requests
from endpoints.test_data import payload
from endpoints.endpoints import Endpoint
from endpoints.token import Token
import allure


class GetMeme(Token, Endpoint):
    my_object_id = None
    text = None

    @allure.step('Check getting one meme')
    def get_one_meme(self, new_meme):
        self.response = requests.get(f'{self.url}/{self.for_all_memes}/{new_meme}', headers=self.headers)
        self.my_object_id = self.response.json()["id"]
        self.text = self.response.json()["text"]
        return self.response

    @allure.step('Check equal id')
    def equal_id(self, new_meme):
        assert new_meme == self.my_object_id, 'Not equal'

    @allure.step('Check equal text')
    def check_text(self):
        assert self.text == payload["text"], 'Not Funny cats'
