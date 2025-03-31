from endpoints.endpoints import Endpoint
import requests


class AllMemes(Endpoint):
    def get_memes(self, new_meme):
        response = requests.get(f'{self.url}/{self.for_all_memes}', headers=self.headers).json()
        self.all_my_memes = [element["id"] for element in response["data"] if element["updated_by"] == "Daniil Katkov"]
        print(self.all_my_memes)
        return self.all_my_memes

    def check_object_id(self, new_meme):
        assert new_meme in self.all_my_memes, "Different values"
