def test_check_authorize(check_authorize):
    check_authorize.get_new_token()
    check_authorize.check_status_code_200()
    check_authorize.check_user_name()
    check_authorize.correct_token()
    check_authorize.check_text_correct_token()

def test_incorrect_token(check_authorize):
    check_authorize.incorrect_token()
    check_authorize.check_status_code_404()

def test_token_with_empty_body(check_authorize):
    check_authorize.empty_body_for_get_token()
    check_authorize.check_status_code_404()

def test_successful_saving_of_token_to_file(check_authorize):
    check_authorize.get_new_token()
    check_authorize.check_status_code_200()
    check_authorize.token_from_file_and_token_from_endpoint_is_equal()
