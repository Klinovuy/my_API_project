def test_check_authorize(check_authorize):
    check_authorize.get_new_token()
    check_authorize.check_status_code()
    check_authorize.check_user_name()


def test_life_token(check_authorize):
    check_authorize.check_token()
    check_authorize.check_status_code()
