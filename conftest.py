import pytest

from endpoints.add_a_new_meme import AddMeme
from endpoints.get_all_memes import AllMemes
from endpoints.get_one_meme import GetMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.token import Token


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
    return Token()

@pytest.fixture()
def new_meme(add_new_object, delete_my_meme):
    add_new_object.add_a_correct_meme()
    yield add_new_object.object_id
    if delete_my_meme.delete_meme(new_meme=add_new_object.object_id).status_code == 404:
        print('Мем удалён ранее')
    else:
        print('Мем успешно удалён')
