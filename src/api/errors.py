from http import HTTPStatus

from werkzeug import Response
from werkzeug.exceptions import HTTPException


class BadRequest(HTTPException):
    def __init__(self, message: str = ''):
        super(BadRequest, self).__init__()
        message = message or f'{HTTPStatus.BAD_REQUEST.phrase} - {HTTPStatus.BAD_REQUEST.description}'
        self.response = Response(
            f'{{"message": "{message}"}}',
            status=HTTPStatus.BAD_REQUEST,
            mimetype='application/json'
        )


class NotFound(HTTPException):
    def __init__(self, message: str = ''):
        super(NotFound, self).__init__()
        message = message or f'{HTTPStatus.NOT_FOUND.phrase} - {HTTPStatus.NOT_FOUND.description}'
        self.response = Response(
            f'{{"message": "{message}"}}',
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )
