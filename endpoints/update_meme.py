import requests
import allure

from endpoints.endpoints import Endpoint
from endpoints.token import Token
from endpoints.test_data import update_payload
from endpoints.test_data import incorrect_tags


class UpdateMeme(Token, Endpoint):
    text = None

    @allure.step('Check updating new meme')
    def correct_update_new_meme(self, new_meme):
        update_payload["id"] = new_meme
        self.response = requests.put(
            f'{self.url}/{self.for_all_memes}/{new_meme}',
            json=update_payload,
            headers=self.headers
        )
        self.text = self.response.json()["text"]
        return self.response

    @allure.step('Check equal text')
    def check_text(self):
        assert self.text == update_payload["text"]

    @allure.step('Check impossible updating a meme with incorrect tags')
    def incorrect_update_new_meme(self, new_meme):
        incorrect_tags["id"] = new_meme
        self.response = requests.put(
            f'{self.url}/{self.for_all_memes}/{new_meme}',
            json=incorrect_tags,
            headers=self.headers
        )
        return self.response.status_code

    @allure.step('Check impossible updating a meme without token')
    def no_token_for_update_meme(self, new_meme):
        update_payload["id"] = new_meme
        self.response = requests.put(f'{self.url}/{self.for_all_memes}/{new_meme}', json=update_payload)
        return self.response.status_code

    @allure.step('Check impossible updating a meme with incorrect token')
    def incorrect_token_for_update_meme(self, new_meme):
        update_payload["id"] = new_meme
        self.response = requests.put(f'{self.url}/{self.for_all_memes}/{new_meme}', json=update_payload,
                                      headers=self.incorrect_headers)
        return self.response.status_code

    @allure.step('Check impossible updating a meme with empty token')
    def empty_token_for_update_meme(self, new_meme):
        update_payload["id"] = new_meme
        self.response = requests.put(f'{self.url}/{self.for_all_memes}/{new_meme}', json=update_payload,
                                      headers=self.empty_headers)
        return self.response.status_code
