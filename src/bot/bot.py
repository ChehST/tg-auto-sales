import os

from dotenv import load_dotenv

load_dotenv()
class Bot:
    def __init__(self):
        self.token = os.getenv('TOKEN_BOT')

