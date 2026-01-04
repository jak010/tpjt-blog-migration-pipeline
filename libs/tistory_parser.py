from __future__ import annotations

from functools import lru_cache
from typing import List, Union, TYPE_CHECKING

from bs4 import Tag, NavigableString

if TYPE_CHECKING:
    from .engine import Engine


class TistoryContentParser:

    def __init__(self, engine):
        self.engine: Engine = engine

    @lru_cache(maxsize=1)
    def _metadata(self):
        """ Tisotry 게시글 메타데이터 """
        soup = self.engine.get_soup()
        metadata = soup.find("div", {"class": "post-meta"})
        return metadata

    def is_secret_post(self):
        soup = self.engine.get_soup()
        protected_form = soup.find("form", {"class": "protected_form"})

        if protected_form and protected_form.text.find("보호"):
            return True
        return False

    def get_created_at(self):
        return self._metadata().find("span", {"class": "date"}).text

    def get_title(self):
        soup = self.engine.get_soup()
        c = soup.find("div", {"class": "hgroup"})
        return c.find("h1").text

    def get_content_source(self) -> List[NavigableString]:
        """ Content의 html 태그 반환 """
        select_tag = "div"
        select_attr = {"class": "tt_article_useless_p_margin contents_style"}

        result = []

        elements = self.engine.get_soup().find(select_tag, select_attr)

        if not elements:
            raise Exception("접근할 수 없는 게시글")

        for element in elements:
            element: Union[Tag, NavigableString]

            if not self._is_passable(element):
                continue

            result.append(element.text)

            # element에 첨부된 이미지가 있는지 체크
            if element.find("span"):
                data_url = element.find("span").get("data-url")
                if data_url:
                    result.append(data_url.replace("&amp;", "&"))

        return result

    def _is_passable(self, element: Union[Tag, NavigableString]) -> bool:  # TODO, 함수명 다시보기
        """ element의 유효성 체크 """
        if isinstance(element, NavigableString):
            _text = element.strip()
            if _text:
                return True
            return False
        if element.text == "\xa0":
            return False
        return True
