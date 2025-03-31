import requests

from endpoints.endpoints import Endpoint


class DeleteMeme(Endpoint):
    def delete_meme(self, new_meme):
        self.response = requests.delete(f'{self.url}/{self.for_all_memes}/{new_meme}', headers=self.headers)
        print(self.response)
        return self.response
