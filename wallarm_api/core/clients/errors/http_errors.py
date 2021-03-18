from requests import HTTPError


class HttpBaseError(HTTPError):
    def __init__(self, response):
        super(HttpBaseError, self).__init__()
        self.response = response
        self.message = ''

    @staticmethod
    def get_text(response):
        if response.text.startswith('"'):
            return response.json()
        return response.text

    def __str__(self):
        return self.message.format(self.get_text(self.response)).strip()


class HttpUnsupportedStatus(HttpBaseError):
    def __init__(self, response):
        super(HttpUnsupportedStatus, self).__init__(response)
        self.message = 'The response contains an unsupported status code: {}'

    def __str__(self):
        return self.message.format(self.response.status_code).strip()


class HttpBadRequest(HttpBaseError):
    def __init__(self, response):
        super(HttpBadRequest, self).__init__(response)
        self.message = 'The request cannot be processed: {}'


class HttpPaymentRequired(HttpBaseError):
    def __init__(self, response):
        super(HttpPaymentRequired, self).__init__(response)
        self.message = 'The request caused an error with code 402: {}'


class HttpUnauthorized(HttpBaseError):
    def __init__(self, response):
        super(HttpUnauthorized, self).__init__(response)
        self.message = 'The request is unauthorized: {}'


class HttpForbidden(HttpBaseError):
    def __init__(self, response):
        super(HttpForbidden, self).__init__(response)
        self.message = 'The server refused to authorize the request: {}'


class HttpNotFound(HttpBaseError):
    def __init__(self, response):
        super(HttpNotFound, self).__init__(response)
        self.message = 'The resource is not found on the server side: {}'


class HttpNotAllowed(HttpBaseError):
    def __init__(self, response):
        super(HttpNotAllowed, self).__init__(response)
        self.message = 'The method is not supported by the target resource: {}'


class HttpNotAcceptable(HttpBaseError):
    def __init__(self, response):
        super(HttpNotAcceptable, self).__init__(response)
        self.message = 'The server cannot respond with the accept-header specified in the request: {}'


class HttpConflict(HttpBaseError):
    def __init__(self, response):
        super(HttpConflict, self).__init__(response)
        self.message = 'This response is sent when a request conflicts with the current state of the server: {}'
