from random import choice
from wordlist import Wordlist

class Code:
    _code: tuple[str, ...]

    def __init__(self, n: str, numeric: bool, wl: Wordlist):
        if numeric:
            self._code: tuple[str, ...] = tuple(str(choice(range(0, 9))) for x in range(int(n)))
        else:
            self._code: tuple[str, ...] = tuple(c for c in wl.get_random_word(int(n)))

    def get_code(self) -> str:
        return "".join((x for x in self._code))

    def check_guess(self, s: str) -> bool:
        return self._code == tuple(x for x in list(s))

    def get_feedback(self, s: str) -> str:
        lst: list[str] = list(s)
        feedback = []

        for i in range(len(lst)):

            if lst[i] == self._code[i]:
                feedback.append(2)
            elif lst[i] in self._code:
                feedback.append(1)
            else:
                feedback.append(0)
        
        feedback.sort(reverse=True)

        return " ".join([str(i) for i in feedback])
