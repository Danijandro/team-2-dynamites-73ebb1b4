from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction
from levelup.gamemap import GameMap
from levelup.position import Position

class TestGameMap(TestCase):
      def test_correct_move_north(self):
        testobj = GameMap()
        self.assertNotEqual(None, testobj.positions)