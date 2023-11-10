from cat import Cat

"""
Tabby class for cat having two attributes
1: name
2: hunger
"""
class Tabby(Cat):
    def __init__(self, name):
        super().__init__(name)

    def feed(self, player):
        """
        Function to feed the cat. It checks
        the cat hunger level and update damage for player
        """
        
        hunger = super()._hunger
        name = super()._name
        if hunger == 5:
            print(
                name, "is pretty hungry and accidentally bites you when it takes the steak from your hand.")
            player.take_damage(3)
        elif hunger < 5:
            print(f"{name} is so hungry that when you set down the steak, Fang mistakes you for food and bites you for {5} damage.")
            player.take_damage(6)
        elif hunger <= 10:
            print(
                f"{name} is so full, when your throw the ball, it lays there sleepily in the sun..")
        super().update_hunger(10)

    def play(self, player):
        """
        Function to play with the cat. It checks
        the cat hunger level and update damage for player
        """
        hunger = super()._hunger
        name = super()._name
        if hunger < 3:
            print(f"{name} is starving, they don't want to play right now. Fang stalks you, chases you down, tackles you, and takes a large chunk out of your arm for {8} damage.")
            player.take_damage(9)
        elif hunger > 7:
            print(f"{name} jumps and plays with the soccer ball you threw, then accidentally tackles you when it comes running back.")
            player.take_damage(19)
            super().update_hunger(hunger - 3)
        else:
            print(f"{name} bit you as they are hungry")
            player.take_damage(6)
            super().update_hunger(hunger - 1)

    def pet(self, player):
        """
        Function to pet the cat. It checks
        the cat hunger level and update damage for player
        """
        hunger = super()._hunger
        name = super()._name
        if hunger > 8:
            print(
                f"{name} is incredibly full and purrs happily as they drift off to sleep.")
            super().update_hunger(hunger - 1)

        elif hunger < 3:
            print(f"{name} bit you as they are hungry")
            player.take_damage(7)
            super().update_hunger(hunger - 1)

        else:
            print(f"{name} happily allows you to pet them.")
            super().update_hunger(hunger - 1)
