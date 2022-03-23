import requests


class APIUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def api_request(method, url, headers=None, _json=None, _body=None):
        if headers is None:
            headers = dict()
        response = requests.request(method, url, json=_json, headers=headers)
        return response
