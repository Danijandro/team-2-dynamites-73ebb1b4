import logging
import sys
from typing import Callable
from levelup.controller import GameController, Direction, InvalidMoveException

VALID_DIRECTIONS = [x.value for x in Direction]

class GameApp:

    controller: GameController

    def __init__(self):
        self.controller = GameController()

    def prompt(self, menu: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{menu}\n> ")
            if validation_fn(response):
                break
        return response

    def game_intro(self):
        while True:
            response = input("\n\n\n\n\n\n\n\nWelcome to the Legendary Dynamites Journey" +
                "\n\nYou will embark on a journey through a jungle filled with tigers, snakes, and dangerous obstacles," +
                "\nwith the goal of finding a golden treasure." +
                "\n\n\n\nAre you ready to begin? (y/n) ")
            if response in ["n","N"]:
                print ("\nHope to see you again soon. Thanks!\n\n\n")
                sys.exit()
            elif response in ["y","Y"]:
                break

    def create_character(self):
        character = self.prompt("What is your name?", lambda x: len(x) > 0)
        self.controller.create_character(character)

    def move_loop(self):
        self.controller.set_character_position((0,0))
        while True:
            response = self.prompt(
                f"Which direction would you like to move? {VALID_DIRECTIONS}\n(or ctrl+c to quit)",
                lambda x: x in VALID_DIRECTIONS,
            )
            direction = Direction(response)
            try:
                self.controller.move(direction)
            except InvalidMoveException:
                print(f"You cannot move {direction}")
            else:
                # TODO: make sure that we are not duplicationg this statement in controller
                print(f"You moved {direction.name}")
            print(self.controller.status)
        

    def start(self):
        self.game_intro()
        self.create_character()
        self.controller.start_game()
        self.move_loop()

    def quit(self):
        print(f"\n\n{self.controller.status}")

