def test_delete_a_new_meme(delete_my_meme, new_meme):
    delete_my_meme.delete_meme(new_meme)
    delete_my_meme.check_status_code()


def test_list_of_all_memes(get_all_memes, new_meme):
    get_all_memes.get_memes(new_meme)
    get_all_memes.check_object_id(new_meme)


def test_get_one_meme(get_new_meme, new_meme):
    get_new_meme.get_one_meme(new_meme)
    get_new_meme.check_status_code()
    get_new_meme.equal_id(new_meme)


def test_update_meme(update_my_meme, new_meme):
    update_my_meme.update_new_meme(new_meme)
    update_my_meme.check_text()
    update_my_meme.check_status_code()


def test_add_my_meme(add_new_object):
    body = {
        "text": "Funny cats",
        "url": "https://kinpet.ru/upload/webp/iblock/5a9/zqfsks555los2ovnmv2vxwyuchdrm7i9/polosatye_koty_fon_jpg.webp",
        "tags": ["cats", "boys", "girls"],
        "info": {"colour": "different", "age": "1-10"}
    }
    add_new_object.add_a_meme(payload=body)
    add_new_object.check_text(body["text"])
