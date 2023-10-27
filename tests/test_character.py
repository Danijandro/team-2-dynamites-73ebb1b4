from unittest import TestCase
from levelup.character import Character

CHARACTER_NAME_ENTERED = "Dynamites"
class TestCharacterInitWithName(TestCase):
    def test_init_character_with_name(self):
        testobj = Character(CHARACTER_NAME_ENTERED)
        self.assertEqual(CHARACTER_NAME_ENTERED, testobj.name)
