from endpoints.endpoints import Endpoint
import requests


class AddMeme(Endpoint):
    def add_a_meme(self, payload):
        self.check_token()
        self.response = requests.post(f'{self.url}/{self.for_all_memes}', json=payload, headers=self.headers)
        self.object_id = self.response.json()["id"]
        self.text = self.response.json()["text"]
        print(self.object_id)
        return self.response

    def check_text(self, text):
        assert self.text == text
