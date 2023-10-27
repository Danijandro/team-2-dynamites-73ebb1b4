from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction
from levelup.gamemap import GameMap
from levelup.position import Position

class TestGameMap(TestCase):
      
      NORTH_DIRECTION=1
      SOUTH_DIRECTION=2
      WEST_DIRECTION=3
      EAST_DIRECTION=4
      def test_correct_move_north(self):
        testobj = GameMap()
        output_position = testobj.calculateposition(Position(0,0),self.NORTH_DIRECTION)
        self.assertEqual(0, output_position.x)
        self.assertEqual(1, output_position.y)

      def test_correct_move_south(self):
        testobj = GameMap()
        output_position = testobj.calculateposition(Position(9,9),self.SOUTH_DIRECTION)
        self.assertEqual(9, output_position.x)
        self.assertEqual(8, output_position.y)   

      def test_correct_move_east(self):
        testobj = GameMap()
        output_position = testobj.calculateposition(Position(7,6),self.EAST_DIRECTION)
        self.assertEqual(8, output_position.x)
        self.assertEqual(6, output_position.y)

      def test_correct_move_west(self):
        testobj = GameMap()
        output_position = testobj.calculateposition(Position(5,5),self.WEST_DIRECTION)
        self.assertEqual(4, output_position.x)
        self.assertEqual(5, output_position.y)         