from unittest import TestCase
from levelup.controller import GameController

# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Game Controller should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)

CHARACTER_NAME = "Dynamites"
class TestGameController(TestCase):
    def test_init_gamecontroller_has_status(self):
        testObj = GameController()
        assert testObj.status != None
        
   
    def test_create_character_has_name(self):
        testObj = GameController()
        testObj.create_character(CHARACTER_NAME)
        assert testObj.status.character_name == CHARACTER_NAME  