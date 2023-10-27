from unittest import TestCase
from levelup.controller import GameController
from levelup.position import Position
from levelup.direction import Direction


# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Game Controller should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)

CHARACTER_NAME = "Dynamites"
DEFAULT_CHARACTER_NAME = "Character"
class TestGameController(TestCase):
    def test_init_gamecontroller_has_status(self):
        testObj = GameController()
        assert testObj.status != None
        
   
    def test_create_character_has_name(self):
        testObj = GameController()
        testObj.create_character(CHARACTER_NAME)
        assert testObj.status.character_name == CHARACTER_NAME 

    def test_create_character_has_default_name(self):
        testObj = GameController()
        testObj.create_character("")
        assert testObj.status.character_name == DEFAULT_CHARACTER_NAME     

    def test_controller_move(self):
        testObj = GameController()
        testObj.status.current_position = (0,0)
        testObj.move(Direction.NORTH)
        assert testObj.status.current_position[0] == 0 
        assert testObj.status.current_position[1] == 1 
        assert testObj.status.move_count == 1      