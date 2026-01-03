import requests
from bs4 import BeautifulSoup

from libs.exceptions import NotAccessableException
from storage.dao import FileDao


class Engine:
    _HEADERS = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
    }

    @classmethod
    def initialize(cls, url: str):
        resp = requests.get(url, headers=cls._HEADERS)
        if resp.status_code != 200:
            raise NotAccessableException()
        return cls(resp.text)

    def __init__(self, page_source):
        self.parser = "html.parser"
        self._page_source = page_source

    def get_soup(self):
        s = BeautifulSoup(self._page_source, self.parser)
        return s
