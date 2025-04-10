__author__ = """730574445"""

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_correct() -> None:
    input: dict[str, str] = {"big": "guy"}
    assert invert(input) == {"guy": "big"}


"""tests function with one key and associated term"""


def test_invert_incorrect() -> None:
    input: dict[str, str] = {"big": "guy", "large": "fella"}
    result = invert(input)
    assert result == {"guy": "big", "fella": "large"}


"""tests function with two keys and associated terms"""


def test_invert_outbound() -> None:
    input: dict[str, str] = {"big": 3}
    result = invert(input)
    assert result != {"guy": "big"}


"""Tests function expected to give a type error"""


def test_count_correct() -> None:
    input: list[str] = ["cat", "dog", "cat", "pigeon"]
    assert count(input) == {"cat": 2, "dog": 1, "pigeon": 1}


"""Tests function with one clear count that is more than one """


def test_count_tie() -> None:
    input: list[str] = ["cat", "dog", "pigeon"]
    assert count(input) == {"cat": 1, "dog": 1, "pigeon": 1}


"""Tests function with all counts just at 1"""


def test_count_outbound() -> None:
    input: list[str] = ["cat", 3]
    result = count(input)
    assert result != {"cat": 1, "dog": 1}


"""Tests function with a type error"""


def test_favorite_color_correct() -> None:
    assert favorite_color({"a": "red", "b": "blue", "c": "red"}) == "red"


"""Tests function with clear favorite"""


def test_favorite_color_tie() -> None:
    assert favorite_color({"a": "red", "b": "blue"}) == "red"


"""Tests function with a tie"""


def test_favorite_color_outbound() -> None:
    assert favorite_color({"a": "red"}) == "red"


"""Tests function with only one key"""


def test_bin_len_correct() -> None:  # use case
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
    """should return correctly """


def test_bin_len_incorrect() -> None:  # use case
    assert bin_len(["the", "tall", "fox"]) == {3: {"the", "fox"}, 4: {"tall"}}


"""Tests function with different words"""


def test_bin_len_outbound() -> None:  # use case
    assert bin_len(["the", "the", "the"]) == {3: {"the"}}


"""Tests function with all same word"""
