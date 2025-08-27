def test_check_authorize(check_authorize):
    check_authorize.get_new_token()
    check_authorize.check_status_code_200()
    check_authorize.check_user_name()
    check_authorize.correct_token()
    check_authorize.check_text()

def test_incorrect_token(check_authorize):
    check_authorize.incorrect_token()
    check_authorize.check_status_code_404()
