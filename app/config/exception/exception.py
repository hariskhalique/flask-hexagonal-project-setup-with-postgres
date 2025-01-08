class AppException(Exception):
    def __init__(self, message=None, status_code=400, details=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}
