import pytest

from endpoints.add_a_new_meme import AddMeme
from endpoints.get_all_memes import AllMemes
from endpoints.get_one_meme import GetMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.endpoints import Endpoint


@pytest.fixture()
def get_all_memes():
    return AllMemes()

@pytest.fixture()
def get_new_meme():
    return GetMeme()

@pytest.fixture()
def add_new_object():
    return AddMeme()

@pytest.fixture()
def update_my_meme():
    return UpdateMeme()

@pytest.fixture()
def delete_my_meme():
    return DeleteMeme()

@pytest.fixture()
def check_authorize():
    return Endpoint()

@pytest.fixture()
def new_meme(add_new_object, get_new_meme, delete_my_meme):
    payload = {
        "text": "Funny cats",
        "url": "https://kinpet.ru/upload/webp/iblock/5a9/zqfsks555los2ovnmv2vxwyuchdrm7i9/polosatye_koty_fon_jpg.webp",
        "tags": ["cats", "boys", "girls"],
        "info": {"colour": "different", "age": "1-10"}
    }
    add_new_object.add_a_meme(payload)
    yield add_new_object.object_id
    if delete_my_meme.delete_meme(new_meme=add_new_object.object_id).status_code == 404:
        print('Мем удалён ранее')
    else:
        print('Мем успешно удалён')
