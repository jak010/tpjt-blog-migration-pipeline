from libs.engine import Engine
from libs.exceptions import NotAccessableException
from libs.tistory_checker import TistoryRSSChecker
from storage.dao import FileDao

rss_check = TistoryRSSChecker()
last_index = rss_check.get_laste_post_index()

file_dao = FileDao()


def initalize_workload():
    """ db.json 초기화 하기 """
    for post_index in range(last_index, 0, -1):
        access_url = f"https://jakpentest.tistory.com/{post_index}"

        try:
            Engine.initialize(access_url)
            file_dao.prepare(post_index)
        except NotAccessableException as e:
            file_dao.unsave(post_index)  # TODO, 260103 : 접근할 수 없는 게시글을 저장할 필요가 있는가 ?
        finally:
            print(f"Progress:{access_url}")
