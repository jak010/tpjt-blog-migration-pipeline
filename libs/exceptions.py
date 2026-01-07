class EngineException(Exception):
    pass


class NotAccessableException(EngineException):
    """ 접근할 수 없는 게시글 """
