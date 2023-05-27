from .clients import *

class Bridge:
    def __init__(self):
        self.discord_client = DiscordClient
        self.matrix_client = MatrixClient

    def start(self):
        print("Started!")
