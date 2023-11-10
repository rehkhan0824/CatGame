"""
Player class for cat having two attributes
1: hp
"""
class Player:
    __hp = 0

    def __init__(self):
        self.__hp = 25

    @property
    def _hp(self):
        return self.__hp

    def take_damage(self, dmg):
        self.__hp = self.__hp - dmg
        if self.__hp < 0:
            self.__hp = 0

    def __str__(self):
        return f"You have {self.__hp} hp."