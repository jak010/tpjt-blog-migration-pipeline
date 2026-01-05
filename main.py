from typing import List

from libs.engine import Engine
from libs.export.template import MarkDownExportTemplate
from libs.llm.gemini import GeminiLLM
from libs.tistory_checker import TistoryRSSChecker
from libs.tistory_parser import TistoryContentParser
from storage.dao import FileDao


class Application:

    def __init__(self):
        self.tistory_rss_checker = TistoryRSSChecker()
        self.dao = FileDao()
        self.llm = GeminiLLM()

    def test(self):
        c = self.dao.update(482, False)
        print(c)

    def get_latest_content(self) -> List[TistoryContentParser]:
        _depth = 3  # 가져올 포스팅 수
        latest_posts = self.dao.get_accessable_post(depth=_depth)

        result = []
        for post in latest_posts:
            result.append(
                TistoryContentParser(
                    Engine.initialize(
                        f"https://jakpentest.tistory.com/{post.get('id')}"
                    )
                )
            )

        return result

    def generated_content(self, content):
        try:
            return self.llm.execute('\n\n'.join(content)).text
        except Exception as e:
            raise e

    def execute(self):
        """ Markdown Export """
        contents = self.get_latest_content()

        content = contents[0]

        generated_content = self.generated_content(
            content.get_content_source()
        )
        if generated_content:
            self.dao.update(content.get_post_number(), True)

        exporter = MarkDownExportTemplate(
            file_name=content.get_title(),
            file_content=self.generated_content(
                content.get_content_source()
            )
        )
        exporter.execute()


if __name__ == '__main__':
    app = Application()
    app.execute()
