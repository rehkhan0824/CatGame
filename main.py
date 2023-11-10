#Name: Rehman Khan
#Date: 10-19-2022
#Description: A game where the player interacts with different types of cats.
from ocelot import Ocelot
from player import Player
from tabby import Tabby
from tiger import Tiger


def interact_cat(cat, player):
    """
    Function to interact with the cat
    The options:
    1: Feed 
    2: Play
    3: Cat
    """
    print(cat)
    print("Cat Menu:")
    print("1. Feed your cat")
    print("2. Play with your cat")
    print("3. Pet your cat")
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            cat.feed(player)
        elif choice == 2:
            cat.play(player)
        elif choice == 3:
            cat.pet(player)
        else:
            print("Invalid choice")
        print(f"\n{player}")
    except ValueError:
        print("Inavlid choice.")
        return


def main():
    """
    Main function to interact with the app
    """
    print("Cat Selection:")
    print("1. Tabby Cat")
    print("2. Ocelot")
    print("3. Tiger")
    try:
        choice = int(input("Enter choice: "))
        if choice < 0 or choice > 3:
            print("Invalid selection. Try again")
            main()
        else:
            name = input("Name your kitty: ")
            player = Player()
            if choice == 1:
                cat = Tabby(name)

            elif choice == 2:
                cat = Ocelot(name)
            else:
                cat = Tiger(name)

            while player._hp != 0:
                interact_cat(cat, player)
            print("Your cat killed you...")
    except ValueError:
        print("Invalid selection. Try again")
        main()


if __name__ == "__main__":
    main()
