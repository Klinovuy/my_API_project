import requests

from endpoints.endpoints import Endpoint


class GetMeme(Endpoint):
    def get_one_meme(self, new_meme):
        self.response = requests.get(f'{self.url}/{self.for_all_memes}/{new_meme}', headers=self.headers)
        self.my_object_id = self.response.json()["id"]
        return self.response

    def equal_id(self, new_meme):
        assert new_meme == self.my_object_id, 'Not equal'
