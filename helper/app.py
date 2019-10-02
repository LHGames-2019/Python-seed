from os import environ
from helper.singleton import Singleton

class Settings(metaclass=Singleton):
    def __init__(self):
        if "LHAPI_URL" not in environ:
            environ["LHAPI_URL"] = "http://localhost:5002"
        self.__lhapi_url = environ["LHAPI_URL"]
        print(f"LHAPI_URL: {self.__lhapi_url}")

        if "GAME_SERVER_URL" not in environ:
            environ["GAME_SERVER_URL"] = "http://localhost:5001"
        self.__game_server_url = environ["GAME_SERVER_URL"]
        print(f"GAME_SERVER_URL: {self.__game_server_url}")

    @property
    def lhapi_url(self):
        return self.__lhapi_url

    @property
    def game_server_url(self):
        return self.__game_server_url
