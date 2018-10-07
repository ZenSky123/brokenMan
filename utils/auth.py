import requests
from lxml import etree

REGISTER_URL = "http://hznu.club/OJ/register.php"
REGISTER_PAGE_URL = "http://hznu.club/OJ/registerpage.php"
LOGIN_URL = "http://hznu.club/OJ/login.php"
LOGIN_PAGE_URL = "http://hznu.club/OJ/loginpage.php"


def register(username, password, cls, nick=''):
    form_data = {
        'csrf_token': '',
        'user_id': username,
        'password': password,
        'rptpassword': password,
        'nick': nick,
        'class': cls,
        'email': '610040513@qq.com',
        'submit': 'Register'
    }
    s = requests.Session()
    req = s.get(REGISTER_PAGE_URL)
    e = etree.HTML(req.text)

    csrf_input = e.xpath('//input[@name="csrf_token"]')[0]
    csrf_token = csrf_input.get('value')
    form_data['csrf_token'] = csrf_token

    s.post(REGISTER_URL, data=form_data)


def login(username, password='123456'):
    form_data = {
        'csrf_token': '',
        'user_id': username,
        'password': password,
        'submit': 'Login'
    }
    s = requests.Session()
    req = s.get(LOGIN_PAGE_URL)
    e = etree.HTML(req.text)

    csrf_input = e.xpath('//input[@name="csrf_token"]')[0]
    csrf_token = csrf_input.get('value')
    form_data['csrf_token'] = csrf_token

    s.post(LOGIN_URL, data=form_data)
    cookies = s.cookies

    return cookies
