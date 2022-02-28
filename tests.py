import pytest
from game import *
from code import *
from wordlist import *

wl: Wordlist = Wordlist()
wl.load_custom_dict({3: ["the", "cat", "hat"], 4: ["comes", "back"]})


def test_load_custom_dict1():
    assert wl.get_length() == 2


def test_load_custom_dict2():
    assert wl.get_list_by_length(4) == ["comes", "back"]


c_obj1: Code = Code("4", True, wl)
c1: str = c_obj1.get_code()


def test_code_constructor1():
    assert len(c1) == 4


def test_code_constructor2():
    assert isinstance(int(c1), int)


g: Game = Game(c_obj1)

c_obj2: Code = Code("4", True, wl)
c2: str = c_obj2.get_code()


def test_code_constructor3():
    assert c1 != c2

def test_get_random_word():
    w: str = wl.get_random_word(3)
    assert w in ["the", "cat", "hat"]