#########################
# DO NOT EDIT THIS FILE #
#########################
from helper.app import Settings
from helper.data import Player, HostPlayer, Team, GameInfo, Map
from helper.singleton import Singleton
from signalrcore.hub_connection_builder import HubConnectionBuilder

class GameServerService(metaclass=Singleton):
    def __init__(self):
        self.__team_id = None
        self.__bot = None

        self.__hub = HubConnectionBuilder() \
            .with_url(Settings().game_server_url + "/teamshub") \
            .with_automatic_reconnect({
                "type": "raw",
                "keep_alive_interval": 10,
                "reconnect_interval": 5,
            }) \
            .build()
        self.__hub.on_open(self.__on_open)
        self.__hub.on_close(self.__on_close)
        self.__hub.on("RequestExecuteTurn", self.__on_request_execute_turn)

    def start(self):
        self.__hub.start()

    def join(self):
        self.__hub.hub._thread.join()

    def __on_open(self):
        print("game server: connection opened and handshake received")

    def __on_close(self):
        print("game server: connection closed")

    def __on_request_execute_turn(self, currentMap, dimension, maxMovement, movementLeft, lastMove, teamNumber):
        if self.__bot == None:
            raise ValueError

        current_map = Map.from_strings(currentMap)

        host_team = teamNumber
        host_position = current_map.get_head_position(host_team)
        host_tail = current_map.get_tail_length(host_team)
        host_body = current_map.get_body_size(host_team)
        host_max_movement = maxMovement
        host_movement_left = movement_left
        host_last_move = lastMove
        host = HostPlayer(
            host_team,
            host_position,
            host_body,
            host_max_movement,
            host_movement_left,
            host_last_move,
        )

        others = []
        for other_team in Team.get_other_teams(host_team):
            other_position = current_map.get_head_position(other_team)
            other_tail = current_map.get_tail_length(other_team)
            other_body = current_map.get_body_size(other_team)
            others.append(Player(
                other_team,
                other_position,
                other_tail,
                other_body,
            ))

        game_info = GameInfo(current_map, host, others)
            
        return self.__bot.get_next_action(game_info)

    def set_bot(self, bot):
        self.__bot = bot

    def set_team_id(self, team_id):
        if self.__team_id is not None:
            print("game server: received team ID multiple times")
        self.__team_id = team_id
        self.__hub.send("Register", team_id)

