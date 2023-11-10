from abc import ABC, abstractmethod

"""
Abstract class for cat having two attributes
1: name
2: hunger
"""
class Cat(ABC):
    def __init__(self, name):
        """
        Constructor to intialize the attributes
        """
        self.__name = name
        self.__hunger = 5

    def update_hunger(self, val):
        """
        Function to update the hunger based on value
        """
        if val >= 1 and val <= 10:
            self.__hunger = val

    def __str__(self):
        """
        __str__ method to get the hunger level and the cat name
        """
        string = f"{self.__name}"
        string += f"\nStarving{'Full':>27}"
        string += f'\n|{" + " *self.__hunger} + {" - " * (10 - self.__hunger)}|'
        return string

    @property
    def _name(self):
        return self.__name

    @property
    def _hunger(self):
        return self.__hunger

    @abstractmethod
    def feed(self, player):
        pass

    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pet(self, player):
        pass