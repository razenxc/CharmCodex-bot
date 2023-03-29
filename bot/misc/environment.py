from abc import ABC
from typing import Final
from os import getenv

class Environment(ABC):
    DISCORD_TOKEN: Final = getenv('DISCORD_TOKEN')
