from enum import Enum, auto

class GameState(Enum):
    START_MENU = auto()
    GAME_IS_ACTIVE = auto()
    PAUSED = auto()
    FIGHTING = auto()