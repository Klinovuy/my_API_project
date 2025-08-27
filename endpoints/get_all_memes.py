from endpoints.endpoints import Endpoint
from endpoints.token import Token
import requests
import allure


class AllMemes(Token, Endpoint):
    all_my_memes = None

    @allure.step('Check getting all memes')
    def get_memes(self):
        self.response = requests.get(f'{self.url}/{self.for_all_memes}', headers=self.headers)
        response = self.response.json()
        self.all_my_memes = [element["id"] for element in response["data"] if element["updated_by"] == "Daniil Katkov"]
        return self.response

    @allure.step('Check that object id is in all memes')
    def check_object_id(self, new_meme):
        assert new_meme in self.all_my_memes, "Different values"
