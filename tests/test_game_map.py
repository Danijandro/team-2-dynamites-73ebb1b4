from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction
from levelup.gamemap import GameMap
from levelup.coordinate import Coordinate

class TestGameMap(TestCase):
      def test_correct_move_north(self):
        testobj = GameMap()
        self.assertNotEqual(None, testobj.positions)