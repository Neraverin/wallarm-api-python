from __future__ import annotations
from abc import ABC, abstractmethod
from json import JSONDecodeError

from wallarm_api.core.clients.errors.http_errors import HttpUnauthorized, HttpNotAllowed, HttpNotFound, \
    HttpForbidden, HttpBadRequest, HttpUnsupportedStatus, HttpPaymentRequired, HttpNotAcceptable, \
    HttpConflict


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, response):
        pass


class BaseHandler(Handler):
    def __init__(self):
        self._next = None

    def set_next(self, handler: Handler) -> Handler:
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, response):
        if self._next:
            return self._next.handle(response)


class DefaultJsonContentHandler(BaseHandler):
    def handle(self, response):
        if len(response.text):
            try:
                result = response.json()
            except JSONDecodeError:
                return response.text
            return result


class OKStatusHandler(BaseHandler):
    def __init__(self):
        self._status_codes = {200, 201, 202, 204, 302}
        super().__init__()

    def handle(self, response):
        if response.status_code in self._status_codes:
            return response
        return super().handle(response)


class NOKStatusHandler(BaseHandler):
    def __init__(self):
        self._status_codes = {}
        super().__init__()

    @staticmethod
    def get_text(response):
        if response.text.startswith('"'):
            return response.json()
        return response.text

    def handle(self, response):
        if response.status_code in self._status_codes:
            raise HttpBadRequest(response)
        return super().handle(response)


class ErrorStatusHandler(BaseHandler):
    def handle(self, response):
        status_code = response.status_code
        if status_code == 400:
            raise HttpBadRequest(response)

        if status_code == 401:
            raise HttpUnauthorized(response)

        if status_code == 402:
            raise HttpPaymentRequired(response)

        if status_code == 403:
            raise HttpForbidden(response)

        if status_code == 404:
            raise HttpNotFound(response)

        if status_code == 405:
            raise HttpNotAllowed(response)

        if status_code == 406:
            raise HttpNotAcceptable(response)

        if status_code == 409:
            raise HttpConflict(response)

        raise HttpUnsupportedStatus(response)
