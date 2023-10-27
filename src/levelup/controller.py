import logging
from dataclasses import dataclass
from enum import Enum
from levelup.gamemap import GameMap
from levelup.position import Position
from levelup.direction import Direction



DEFAULT_CHARACTER_NAME = "Character"
directionMap={Direction.NORTH:1, Direction.SOUTH:2, Direction.WEST:3, Direction.EAST:4};

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (-100,-100)
    move_count: int = 0

    def _str_(self) -> str:
        return f"{self.character_name} is currently on {self.current_position} and have moved {self.move_count} steps."

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
        update_position: Position = self.gameMap.calculateposition(Position(self.status.current_position[0],self.status.current_position[1]),directionMap.get(direction))
        self.set_character_position((update_position.x,update_position.y))
        self.set_current_move_count(self.status.move_count)
        

    def set_character_position(self, xycoordinates: tuple) -> None:
        self.status.current_position = xycoordinates


    def set_current_move_count(self, move_count: int) -> None:
          self.status.move_count = move_count+1;
           

    def get_total_positions(self) -> int:
        print("this is in get_total_positions")
        return  self.status.move_count

    
