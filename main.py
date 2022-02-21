import sys
from code import Code
from game import Game


def length_prompt() -> str:
    print("Code length (0-9): ", end="")
    valid = False
    n = input()
    while not valid:
        try:
            int(n)
            valid = True
        except ValueError or len(n) > 1:
            print("Please enter the code length as a single-digit number: ", end="")
            n = input()
        except int(n) < 1:
            print("The code needs to be at least one char long: ", end="")
            n = input()
    return n


def type_prompt() -> bool:
    print("Numeric (1) or verbal (2)? ", end="")
    valid = False
    n = input()
    while not valid:
        try:
            n = int(n)
            if n == 1 or n == 2:
                valid = True
            else:
                print("Please indicate your choice by entering 1 or 2: ", end="")
                n = input()
        except:
            print("Please indicate your choice by entering 1 or 2: ", end="")
            n = input()
    return n == 1


def main():
    n = length_prompt()
    numeric = type_prompt()
    this_code: Code = Code(n, numeric)
    this_game: Game = Game(this_code)
    again = this_game.run()
    while again:
        n = length_prompt()
        this_code: Code = Code(n)
        this_game.reload_code(this_code)
        again = this_game.run()

    sys.exit()


if __name__ == '__main__':
    main()
