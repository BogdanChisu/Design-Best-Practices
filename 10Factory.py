"""
-------------------------------------------------------------------------------
FACTORY METHOD Creational Pattern
-------------------------------------------------------------------------------

https://refactoring.guru/design-patterns/factory-method

FACTORY METHOD

Factory Method is a creational design pattern that provides an interface for
creating objects in a superclass, but allows subclassed to alter the type of
objects that will be created.
"""

class Game:
    def get_name(self):
        pass

    def get_type(self):
        pass


class BoardGame(Game):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def get_name(self):
        return self.name

    def get_name(self):
        return self.type

    def __str__(self):
        return f"{__name__} [name='{self.name}', type='{self.type}']"


class PCGame(Game):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def __str__(self):
        return f"{__name__} [name='{self.name}', type='{self.type}']"


class GameFactory:
    def create(self):
        pass


class MonopolyGameCreator(GameFactory):
    def create(self):
        return BoardGame("Monopoly", "10-15 Ani")


class ValorantGameCreator(GameFactory):
    def create(self):
        return  PCGame("Valorant", "V2.3")

game = MonopolyGameCreator()
game.create()
print(game.create())