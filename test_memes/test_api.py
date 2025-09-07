from endpoints.test_data import incorrect_text
from endpoints.test_data import incorrect_url
from endpoints.test_data import incorrect_tags
from endpoints.test_data import incorrect_info
from endpoints.test_data import update_payload
from endpoints.test_data import payload
import pytest


def test_delete_a_new_meme(delete_my_meme, get_new_meme, new_meme):
    delete_my_meme.delete_meme(new_meme)
    delete_my_meme.check_status_code_200()
    get_new_meme.get_one_meme(new_meme)
    get_new_meme.check_status_code_404()

def test_no_authorization_for_delete_meme(delete_my_meme, new_meme):
    delete_my_meme.no_token_for_delete_meme(new_meme)
    delete_my_meme.check_status_code_401()

def test_incorrect_authorization_for_delete_meme(delete_my_meme, new_meme):
    delete_my_meme.incorrect_token_for_delete_meme(new_meme)
    delete_my_meme.check_status_code_401()

def test_empty_authorization_for_delete_meme(delete_my_meme, new_meme):
    delete_my_meme.empty_token_for_delete_meme(new_meme)
    delete_my_meme.check_status_code_500()

def test_list_of_all_memes(get_all_memes, new_meme):
    get_all_memes.get_memes()
    get_all_memes.check_object_id(new_meme)
    get_all_memes.check_status_code_200()

def test_no_authorization_for_get_all_memes(get_all_memes):
    get_all_memes.no_token_for_get_memes()
    get_all_memes.check_status_code_401()

def test_incorrect_authorization_for_get_all_memes(get_all_memes):
    get_all_memes.incorrect_token_for_get_memes()
    get_all_memes.check_status_code_401()

def test_empty_authorization_for_get_all_memes(get_all_memes):
    get_all_memes.empty_token_for_get_memes()
    get_all_memes.check_status_code_500()

def test_get_one_meme(get_new_meme, new_meme):
    get_new_meme.get_one_meme(new_meme)
    get_new_meme.check_status_code_200()
    get_new_meme.equal_id(new_meme)
    get_new_meme.check_text()

def test_no_authorization_for_get_one_meme(get_new_meme, new_meme):
    get_new_meme.no_token_for_get_memes(new_meme)
    get_new_meme.check_status_code_401()

def test_incorrect_authorization_for_get_one_meme(get_new_meme, new_meme):
    get_new_meme.incorrect_token_for_get_memes(new_meme)
    get_new_meme.check_status_code_401()

def test_empty_authorization_for_get_one_meme(get_new_meme, new_meme):
    get_new_meme.empty_token_for_get_memes(new_meme)
    get_new_meme.check_status_code_500()

def test_correct_update_meme(update_my_meme, new_meme):
    update_my_meme.correct_update_new_meme(new_meme)
    update_my_meme.check_text(update_payload["text"])
    update_my_meme.check_url(update_payload["url"])
    update_my_meme.check_tags(update_payload["tags"])
    update_my_meme.check_info(update_payload["info"])
    update_my_meme.check_object_id()
    update_my_meme.check_status_code_200()

def test_no_authorization_for_update_meme(update_my_meme, new_meme):
    update_my_meme.no_token_for_update_meme(new_meme)
    update_my_meme.check_status_code_401()

def test_incorrect_authorization_for_update_meme(update_my_meme, new_meme):
    update_my_meme.incorrect_token_for_update_meme(new_meme)
    update_my_meme.check_status_code_401()

def test_empty_authorization_for_update_meme(update_my_meme, new_meme):
    update_my_meme.empty_token_for_update_meme(new_meme)
    update_my_meme.check_status_code_500()

def test_add_correct_meme(add_new_object, new_meme):
    add_new_object.check_text(payload["text"])
    add_new_object.check_url(payload["url"])
    add_new_object.check_tags(payload["tags"])
    add_new_object.check_info(payload["info"])
    add_new_object.check_status_code_200()

def test_no_authorization_for_add_correct_meme(add_new_object):
    add_new_object.no_token_for_add_a_new_meme()
    add_new_object.check_status_code_401()

def test_incorrect_authorization_for_add_correct_meme(add_new_object):
    add_new_object.incorrect_token_for_add_a_new_meme()
    add_new_object.check_status_code_401()

def test_empty_authorization_for_add_correct_meme(add_new_object):
    add_new_object.empty_token_for_add_a_new_meme()
    add_new_object.check_status_code_500()

@pytest.mark.parametrize("incorrect_data", [incorrect_text, incorrect_url, incorrect_tags, incorrect_info])
def test_add_incorrect_meme(add_new_object, incorrect_data):
    add_new_object.add_an_incorrect_meme(incorrect_data)
    add_new_object.check_status_code_400()
