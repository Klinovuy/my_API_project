import requests
import allure

from endpoints.endpoints import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Check deleting a new meme')
    def delete_meme(self, new_meme):
        self.response = requests.delete(f'{self.url}/{self.for_all_memes}/{new_meme}', headers=self.headers)
        return self.response

    @allure.step('Check correct deleting a new meme')
    def check_delete_meme(self, new_meme):
        assert self.response.text == f'Meme with id {new_meme} successfully deleted',\
            f"Meme with id {new_meme} doesn't delete"

    @allure.step('Check impossible deleting meme without token')
    def no_token_for_delete_meme(self, new_meme):
        self.response = requests.delete(f'{self.url}/{self.for_all_memes}/{new_meme}')
        return self.response.status_code

    @allure.step('Check impossible deleting meme with incorrect token')
    def incorrect_token_for_delete_meme(self, new_meme):
        self.response = requests.delete(f'{self.url}/{self.for_all_memes}/{new_meme}',
                                        headers=self.incorrect_headers)
        return self.response.status_code

    @allure.step('Check impossible deleting meme with empty token')
    def empty_token_for_delete_meme(self, new_meme):
        self.response = requests.delete(f'{self.url}/{self.for_all_memes}/{new_meme}', headers=self.empty_headers)
        return self.response.status_code
