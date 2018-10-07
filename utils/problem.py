import requests
from .utils import load_cookies

from lxml import etree


def _e(url, cookies=None):
    req = requests.get(url, cookies=cookies)
    content = req.content
    e = etree.HTML(content)
    return e


class ProblemSystem:
    def __init__(self, problem_id):
        problem_url = "http://hznu.club/OJ/problem.php?id={}".format(problem_id)
        e = _e(problem_url)

        score = float(e.xpath('/html/body/div/div[3]/span[3]/text()')[0])
        title = e.xpath('/html/body/div/h1/text()')[0].strip()

        self.score = score
        self.title = title
        self.problem_id = problem_id
        self.code = self.get_code()

    def get_code(self):
        admin_cookies = load_cookies()

        statics_url = "http://hznu.club/OJ/problemstatus.php?language=0&id={}".format(self.problem_id)
        e = _e(statics_url, admin_cookies)
        run_id = e.xpath('//td/text()')[0]

        source_url = "http://hznu.club/OJ/showsource.php?id={}".format(run_id)
        e = _e(source_url, admin_cookies)

        return ''.join(e.xpath('//code/text()'))

    def ac(self, cookies):
        s = requests.session()
        s.cookies.update(cookies)

        submit_url = "http://hznu.club/OJ/submitpage.php?id={}".format(self.problem_id)
        req = s.get(submit_url)
        e = etree.HTML(req.content)
        csrf = e.xpath('//input[@name="csrf_token"]/@value')[0]

        submit_origin = " http://hznu.club/OJ/submit.php"
        s.post(submit_origin, data={
            'csrf_token': csrf,
            'language': 0,
            'theme': '',
            'source': self.code,
            'id': self.problem_id
        })
