"""Island."""

import requests
import re
import pytesseract
from PIL import Image
from io import BytesIO


class NCULib(object):
    """NCULib."""

    main_url = "http://210.35.251.243/reader/"
    login_page = main_url + 'login.php'
    captcha_url = main_url + 'captcha.php'
    verify_url = main_url + 'redr_verify.php'
    book_list = main_url + 'book_lst.php'

    def __init__(self, username, password):
        """Initialize."""
        self.username = username
        self.password = password
        resp = requests.get(NCULib.login_page)
        self.cookie = dict(resp.cookies)
        self.login()

    def get_captcha(self):
        u"""获取并解析验证码."""
        resp = requests.get(NCULib.captcha_url, cookies=self.cookie)
        image = Image.open(BytesIO(resp.content))
        captcha = pytesseract.image_to_string(image)
        return captcha

    def login(self):
        u"""登录."""
        captcha = self.get_captcha()

        form_data = {
            'number': self.username,
            'passwd': self.password,
            'captcha': captcha,
            'select': 'cert_no',
        }

        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        login_resp = requests.post(NCULib.verify_url, headers=header,
                                   data=form_data, cookies=self.cookie)
        login_resp.encoding = 'utf-8'
        return login_resp.text

    def get_books(self):
        """."""
        resp = requests.get(NCULib.book_list, cookies=self.cookie)
        resp.encoding = 'utf-8'
        return resp.text
