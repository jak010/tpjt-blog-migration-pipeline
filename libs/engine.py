import requests
from bs4 import BeautifulSoup

from libs.exceptions import NotAccessableException
from libs.tistory_parser import TistoryContentParser


class Engine:
    _HEADERS = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
    }

    @classmethod
    def initialize(cls, url: str):
        print(url)
        resp = requests.get(url, headers=cls._HEADERS)
        if resp.status_code != 200:
            raise NotAccessableException()

        _klass = cls(resp.text, url)

        parser = TistoryContentParser(_klass)
        if parser.is_secret_post():
            raise NotAccessableException()

        return _klass

    def __init__(self, page_source, url):
        self.parser = "html.parser"
        self._page_source = page_source
        self._url = url

    def get_soup(self):
        s = BeautifulSoup(self._page_source, self.parser)
        return s

    def get_url(self):
        return self._url
