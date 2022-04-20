class APIMethods:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

    header_application_json = "application/json"


class CommonConstants:
    ui = 'ui_datetime_format'
    utc = 'utc_datetime_format'
    nsc = 'no_special_chars_datetime_format'
    _utc_datetime_format_ = '%Y-%m-%dT%H:%M:%SZ'
    _ui_datetime_format_ = '%Y-%m-%d %H:%M:%S'
    _no_special_chars_datetime_format_ = '%Y%m%d%H%M%S'


class Encryption:
    api_secret_key = 'VSgqZfmtvsCzf8oGLjT660AfpVU2CGYb'
    algorithm = 'HS256'
