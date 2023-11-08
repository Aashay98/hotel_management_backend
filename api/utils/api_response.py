EXPECTION_ERROR_CODE= 400
UNAUTHORIZED_ERROR_CODE = 401
SUCCESS_CODE = 201
NOT_FOUND = 404


class APIResponse:
    def error(self, message, error):
        return {
            'error': error,
            'status': EXPECTION_ERROR_CODE,
            'message': message,
            'data': None
        }, EXPECTION_ERROR_CODE

    def unauthorized(self, message):
        return {
            'error': {
                "status": UNAUTHORIZED_ERROR_CODE
            },
            'message': message,
            'data': None,
            'status': UNAUTHORIZED_ERROR_CODE
        }, UNAUTHORIZED_ERROR_CODE

    def ok(self, message, data):
        return {
            'error': None,
            'message': message,
            'data': data,
            'status': SUCCESS_CODE
        }, SUCCESS_CODE
