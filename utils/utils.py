import pickle
import os.path
from .auth import login
from .config import config

from requests import get


def hav_admin_logged(cookies):
    url = "http://hznu.club/OJ/admin/index.php"
    req = get(url, cookies=cookies)
    return 'Premission Denied! Please Log in!' not in req.content.decode()


def save_cookies(cookies, filename='data/cookies.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(cookies, f)


def load_cookies(filename='data/cookies.pkl'):
    if not os.path.exists(filename):
        return None
    with open(filename, 'rb') as f:
        cookies = pickle.load(f)
    return cookies


def refresh_admin_cookies():
    cookies = load_cookies()
    if cookies is None or not hav_admin_logged(cookies):
        admin_username = config['admin_username']
        admin_password = config['admin_password']
        cookies = login(admin_username, admin_password)
        save_cookies(cookies)
    return cookies
