import os
import singleton

class Settings(metaclass=singleton.Singleton):
    def __init__(self):
        if "LHAPI_URL" not in os.environ:
            raise ValueError("LHAPI_URL is not defined in environment variables")
        self.__lhapi_url = os.environ["LHAPI_URL"]
        print(f"LHAPI_URL: {self.__lhapi_url}")

        if "GAME_SERVER_URL" not in os.environ:
            raise ValueError("GAME_SERVER_URL is not defined in environment variables")
        self.__game_server_url = os.environ["GAME_SERVER_URL"]
        print(f"GAME_SERVER_URL: {self.__game_server_url}")

    @property
    def lhapi_url(self):
        return self.__lhapi_url

    @property
    def game_server_url(self):
        return self.__game_server_url
