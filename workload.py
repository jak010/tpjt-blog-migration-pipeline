from libs.engine import Engine
from libs.exceptions import NotAccessableException
from libs.tistory_checker import TistoryRSSChecker
from storage.dao import FileDao

rss_check = TistoryRSSChecker()
last_index = rss_check.get_laste_post_index()

file_dao = FileDao()


def initalize_workload():
    """ db.json 초기화 하기 """

    start_index = last_index
    end_index = 0

    for post_index in range(start_index, end_index, -1):
        access_url = f"https://jakpentest.tistory.com/{post_index}"
        print(f"Progress:{access_url}")

        try:
            Engine.initialize(access_url)
        except NotAccessableException as e:
            file_dao.unsave(post_index)  # TODO, 260103 : 접근할 수 없는 게시글을 저장할 필요가 있는가 ?
            continue

        file_dao.prepare(post_index)


if __name__ == '__main__':
    initalize_workload()
