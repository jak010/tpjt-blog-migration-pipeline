import datetime
import json
from typing import Optional

from libs.exceptions import AlreadySavedException


class FileDao:

    def __init__(self):
        self.file_path = "./storage/db.json"

    def load(self):
        with open(self.file_path, "r+", encoding="utf-8") as f:
            return json.load(f)

    def get_accessable_post(self, depth: int = 5):
        """ 접근 가능한 게시글 가져오기

        depth : 최근 게시글에서부터 가져올 item 수
        """
        with open(self.file_path, "r+", encoding="utf-8") as f:
            storage = json.load(f)

            result = []
            for each in storage:
                item = storage.get(each)

                if not item.get("is_saved"):
                    result.append(item)

            return result[:depth + 1]

    def prepare(self, save_index: str):
        """ 저장 대상인 데이터 초기화 """
        _index = str(save_index)

        with open(self.file_path, "r+", encoding="utf-8") as f:
            storage = json.load(f)
            if storage.get(_index):
                raise AlreadySavedException("이미 저장된 게시글")

            _data = self._initialize(_index, is_saved=None)
            storage.update(_data)

            f.seek(0)
            f.flush()
            f.write(json.dumps(storage))

    def unsave(self, save_index: str):
        """ 저장할 수 없는 게시글 초기화 """
        _index = str(save_index)

        with open(self.file_path, "r+", encoding="utf-8") as f:
            storage = json.load(f)
            if storage.get(_index):
                raise AlreadySavedException("이미 저장된 게시글")

            _data = self._initialize(_index, is_saved=False)

            storage.update(_data)
            f.seek(0)
            f.flush()
            f.write(json.dumps(storage))

    def _initialize(self, index, is_saved: Optional[bool] = None):
        """ 데이터 저장하기

        is_saved
          - None : 저장 대상인 게시글
          - False: 접근할 수 없는 게시글
          - True : 저장이 완료된 게시글
        """
        return {
            index:
                {
                    "id": index,
                    "is_saved": is_saved,
                    "created_at": datetime.datetime.now().isoformat()
                }
        }
