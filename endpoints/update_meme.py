import requests

from endpoints.endpoints import Endpoint


class UpdateMeme(Endpoint):
    def update_new_meme(self, new_meme):
        self.payload = {
            "id": new_meme,
            "text": "Great people",
            "url": "https://www.biografguru.ru/img/4420_cnt_bgr.jpg",
            "tags": ["people", "young", "old"],
            "info": {"nationality": "different", "age": "30-80"}
        }
        self.response = requests.put(
            f'{self.url}/{self.for_all_memes}/{new_meme}',
            json=self.payload,
            headers=self.headers
        )
        self.text = self.response.json()["text"]
        return self.response

    def check_text(self):
        assert self.text == self.payload["text"]
