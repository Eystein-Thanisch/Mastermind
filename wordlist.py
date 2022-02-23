from random import choice


class Wordlist:
    _words: dict[int, list[str]]

    def __init__(self):
        self._words = dict()

    def load_words(self):
        f = open("engWordsShort.txt", "r")
        temp = f.read().splitlines()
        for w in temp:
            l = len(w)
            if l not in self._words:
                self._words[l] = list()
            self._words[l].append(w)
        f.close()

    def get_random_word(self, l: int) -> str:
        return choice(self._words[l])

    def get_length(self) -> int:
        return len(self._words.keys())

    def get_list_by_length(self, l: int) -> list[str]:
        return self._words[l]
