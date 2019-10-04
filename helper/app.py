from os import environ
from helper.singleton import Singleton

class Settings(metaclass=Singleton):
    def __init__(self):
        if "LHAPI_URL" in environ:
            self.__lhapi_url = environ["LHAPI_URL"]
        else:
            self.__lhapi_url = None
        print(f"LHAPI_URL: {self.__lhapi_url}")

        if "GAME_SERVER_URL" in environ:
            self.__game_server_url = environ["GAME_SERVER_URL"]
        else:
            self.__game_server_url = None
        print(f"GAME_SERVER_URL: {self.__game_server_url}")

    @property
    def lhapi_url(self):
        return self.__lhapi_url

    @property
    def game_server_url(self):
        return self.__game_server_url

    @game_server_url.setter
    def game_server_url(self, url):
        self.__game_server_url = url
