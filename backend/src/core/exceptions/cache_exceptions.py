class CacheIdentificationInferenceError(Exception):
    """
    Exception raised when the system could not infer the id for the resource being cached.
    """

    def __init__(self, message: str = "Could not infer id for resource being cached.") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidRequestError(Exception):
    """
    Exception raised when the type of request is not supported.
    """

    def __init__(self, message: str = "Type of request not supported.") -> None:
        self.message = message
        super().__init__(self.message)


class MissingClientError(Exception):
    """
    Exception raised when the client is None.
    """

    def __init__(self, message: str = "Client is None.") -> None:
        self.message = message
        super().__init__(self.message)
