from code import Code


class Game:
    _code: Code
    _guesses: int

    def __init__(self, code: Code):
        self._code = code

    def reload_code(self, code: Code):
        self._code = code

    def run(self) -> bool:
        guesses = len(self._code.get_code()) * 3
        print("Code set.")
        print("You can now try and guess the code. You will receive feedback on your answers:")
        print()
        print("     2 : a char in your guess matches the value and location of a char in the code.")
        print("     1 : a char matches the value of a char somewhere else")
        print("     0 : a char in your guess is incorrect in terms of location and value.")
        print()
        print(str(guesses) + " guesses")
        print("Enter the code (" + "x" * len(self._code.get_code()) + "): ", end="")
        guess = input()
        valid = False
        while not valid:
            if len(guess) != len(self._code.get_code()):
                print("The code is " + str(len(self._code.get_code())) + " chars long: ", end="")
                guess = input()
                if guess == "QUIT":
                    return False
            else:
                valid = True

        solved = self._code.check_guess(guess)

        end_string = "Correct! "

        while not solved:
            print(self._code.get_feedback(guess))
            if guesses > 1:
                print(str(guesses) + " guesses left")
            elif guesses == 1:
                print("Last guess!")
            print()
            print("Enter the code (" + "x" * int(len(self._code.get_code())) + "): ", end="")
            guess = input()
            if guess == "QUIT":
                return False
            valid = False
            while not valid:
                if len(guess) != int(len(self._code.get_code())):
                    print("The code is " + str(len(self._code.get_code())) + " chars long: ", end="")
                    guess = input()
                else:
                    valid = True
            solved = self._code.check_guess(guess)
            if not solved and guesses == 1:
                end_string = "Out of guesses. "
                break
            else:
                guesses -= 1

        print(end_string + self._code.get_code())
        print("Play again (y or n)? ", end="")
        r = input()
        if r == "n":
            return False
        return True
