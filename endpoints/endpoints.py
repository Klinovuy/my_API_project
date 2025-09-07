import allure


class Endpoint:
    url = 'http://167.172.172.115:52355/'
    response = None
    my_token = None
    headers = {"Authorization": "token"}
    empty_headers = {"Authorization": ""}
    incorrect_headers = {"Authorization": "test"}
    user = None
    for_all_memes = 'meme'
    text = None
    url_meme = None
    tags = None
    info = None

    @allure.step('Check status code 200')
    def check_status_code_200(self):
        assert self.response.status_code == 200, 'Not 200'

    @allure.step('Check status code 400')
    def check_status_code_400(self):
        assert self.response.status_code == 400, 'Not 400'

    @allure.step('Check status code 401')
    def check_status_code_401(self):
        assert self.response.status_code == 401, 'Not 401'

    @allure.step('Check status code 500')
    def check_status_code_500(self):
        assert self.response.status_code == 500, 'Not 500'

    @allure.step('Check status code 404')
    def check_status_code_404(self):
        assert self.response.status_code == 404, 'Not 404'

    @allure.step('Check equal text')
    def check_text(self, text):
        assert self.text == text

    @allure.step('Check equal url')
    def check_url(self, url):
        assert self.url_meme == url

    @allure.step('Check equal tags')
    def check_tags(self, tags):
        assert self.tags == tags

    @allure.step('Check equal info')
    def check_info(self, info):
        assert self.info == info
