from pip._vendor import requests

class Client:
    def __init__(self, host):
        self._session=requests.Session()
        self._host=host
        answer=requests.get(host, "")
        print(answer.url)
        print(answer.headers)
        print(answer.request.headers)
    def __del__(self):
        self._session.close()

Client('https://httpbin.org')