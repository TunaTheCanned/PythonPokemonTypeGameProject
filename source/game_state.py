from enum import Enum, auto

class GameState(Enum):
    START_MENU = auto()
    FIGHTING = auto()
    CREATURE_SELECTION = auto()
    MESSAGE = auto()