import logging
from dataclasses import dataclass
from enum import Enum
from levelup.gamemap import GameMap
from levelup.position import Position


DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (0,0)
    move_count: int = 0

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


directionMap={Direction.NORTH:1,Direction.SOUTH:2,Direction.WEST:3,Direction.EAST:4};
class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:


    status: GameStatus
    gameMap: GameMap

    def __init__(self):
        self.status = GameStatus()
        self.gameMap = GameMap()

    def start_game(self):
        pass

    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.status.character_name = character_name
        else:
            self.status.character_name = DEFAULT_CHARACTER_NAME

    def move(self, direction: Direction) -> None:
        print(f"You moved {direction.name}")
        print(f"You status {self.status}")
        update_position: Position = self.gameMap.calculateCordinates(Position(self.status.current_position[0],self.status.current_position[1]),directionMap.get(direction))
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        self.status.current_position = (update_position.x,update_position.y)
        pass

    def set_character_position(self, xycoordinates: tuple) -> None:
        print("this is in set_character_position")
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        pass

    def set_current_move_count(self, move_count: int) -> None:
        print("this is in set_current_move_count")
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        pass

    def get_total_positions(self) -> int:
        print("this is in get_total_positions")
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return -10

    
