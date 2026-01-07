from typing import List

from libs.engine import Engine
from libs.export.template import MarkDownExportTemplate
from libs.llm.gemini import GeminiLLM
from libs.tistory import (
    TistoryRSSChecker,
    TistoryContentParser,
    TistoryPostDTO
)
from storage.dao import FileDao


class Application:

    FETCH_SIZE = 3 # 가져올 포스팅 수

    def __init__(self):
        self.tistory_rss_checker = TistoryRSSChecker()
        self.dao = FileDao()
        self.llm = GeminiLLM()

    def get_latest_content(self) -> List[TistoryPostDTO]:
        latest_posts = self.dao.get_accessable_post(depth=self.FETCH_SIZE)

        result: List[TistoryPostDTO] = []
        for post in latest_posts:
            parser = TistoryContentParser(
                Engine.initialize(
                    f"https://jakpentest.tistory.com/{post.get('id')}"
                )
            )

            result.append(parser.to_post())

        return result

    def generated_content(self, content):
        try:
            return self.llm.execute('\n\n'.join(content)).text
        except Exception as e:
            raise e

    def execute(self):
        """ Markdown Export """

        tistory_posts = self.get_latest_content()
        tistory_post = tistory_posts[0]

        generated_content = self.generated_content(
            tistory_post.content
        )
        if generated_content:
            self.dao.update(tistory_post.post_number, True)

        exporter = MarkDownExportTemplate(
            file_name=tistory_post.title,
            file_content=self.generated_content(
                tistory_post.content
            )
        )
        exporter.execute()


if __name__ == '__main__':
    app = Application()
    app.execute()
