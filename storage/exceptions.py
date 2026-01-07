class DaoException(Exception):
    """ File Crud Exception """


class AlreadySavedException(DaoException):
    """ 이미 저장된 게시글 """