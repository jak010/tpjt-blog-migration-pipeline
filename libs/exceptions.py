class EngineException(Exception):
    pass


class NotAccessableException(EngineException):
    """ 접근할 수 없는 게시글 """


class DaoException(Exception):
    """ File Crud Exception """


class AlreadySavedException(DaoException):
    """ 이미 저장된 게시글 """
