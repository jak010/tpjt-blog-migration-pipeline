from __future__ import annotations

from functools import lru_cache
from typing import List, Union, TYPE_CHECKING

from bs4 import Tag, NavigableString

from .tistory_post_dto import TistoryPostDTO

if TYPE_CHECKING:
    from libs.engine import Engine


class TistoryContentParser:
    """ 티스토리 포스팅 데이터 """

    def __init__(self, engine):
        self.engine: Engine = engine

    def to_post(self) -> TistoryPostDTO:
        """ Parser 데이터를 DTO로 변환하기 """
        return TistoryPostDTO(
            title=self._get_title(),
            created_at=self._get_created_at(),
            content="\n".join(self._get_content_source()),
            post_number=self._get_post_number(),
        )

    def _get_post_number(self):
        url = self.engine.get_url()
        post_number = url.split("/")[-1]

        return post_number

    @lru_cache(maxsize=1)
    def _metadata(self):
        """ Tisotry 게시글 메타데이터 """
        soup = self.engine.get_soup()
        metadata = soup.find("div", {"class": "post-meta"})
        return metadata

    def is_secret_post(self):
        """ 비밀글 체크 """
        soup = self.engine.get_soup()
        protected_form = soup.find("form", {"class": "protected_form"})

        if protected_form and protected_form.text.find("보호"):
            return True
        return False

    def _get_created_at(self):
        """ 포스팅 생성일 가져오기 """
        return self._metadata().find("span", {"class": "date"}).text

    def _get_title(self):
        """ 포스팅 제목 가져오기 """
        soup = self.engine.get_soup()
        c = soup.find("div", {"class": "hgroup"})
        return c.find("h1").text

    def _get_content_source(self) -> List[NavigableString]:
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
