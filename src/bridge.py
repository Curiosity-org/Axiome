from .clients import *
from .configuration import get_config

class Bridge:
    def __init__(self):
        self.discord_client = DiscordClient
        self.matrix_client = MatrixClient

    def start(self):
        print("Started!")
        print(get_config('test', 'value'))
