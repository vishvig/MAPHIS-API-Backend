class MaphisException(Exception):
    pass


class MaphisEndpointException(MaphisException):
    """
        A class to create custom error exception

        Args:
            error_type(str): this is the error type generated like 'Internal server error'
            status(int): HTTP status code starts from 400
            message(Any): Error message if any, default is 'something went wrong'

        Notes:
            See https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers
            for more info on creating custom error handlers
        """

    def __init__(self, error_type: str = "Internal Server Error", status: int = 500, message='Something went wrong'):
        self.type = error_type
        self.message = message
        self.status = status
