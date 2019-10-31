class ServiceError(Exception):
    """This class defines the base error of the application"""

    def __init__(self, message):
        self.message = message


class ServiceBodyError(ServiceError):
    """This class defines the specific key/value error of a view handler"""

    def __init__(self, message='Invalid body', status_code=400):
        super().__init__(str(message).replace('\n', ''))
        self.status_code = status_code
