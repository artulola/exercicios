from enum import Enum

class Person:

    def __init__(self, name, age):
        self.name = name
        if 1 <= age <= 150:
            self.age = age
        else:
            raise ValueError("A idade precisa estar no intervalo [1,150]")

    def __str__(self):
        return f"{self.name}({self.age})"
    

class Hobby:

    def __init__(Enum):
        MUSIC = 1
        SPORTS = 2
        GAMES = 3