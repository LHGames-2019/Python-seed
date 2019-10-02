#########################
# DO NOT EDIT THIS FILE #
#########################
from bot import Bot
from helper.game_server import GameServerService
from helper.lhapi import LHAPIService

if __name__ == '__main__':
    bot = Bot()

    GameServerService().set_bot(bot)
    GameServerService().start()
    LHAPIService().start()

    GameServerService().join()
    LHAPIService().join()
