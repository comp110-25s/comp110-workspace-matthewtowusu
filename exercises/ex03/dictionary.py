__author__ = """730574445"""


def invert(init: dict[str, str]) -> dict[str, str]:
    placeholder = ""
    placedict: dict[str, str] = {}
    for key in init:
        if init[key] in placedict:
            raise KeyError("nice try buddy")
        else:
            placeholder = key
            placedict[init[key]] = placeholder
    return placedict


def count(input: list[str]) -> dict[str, int]:
    newdict: dict[str, int] = {}
    x = 0
    while x < len(input):
        if input[x] in newdict:
            newdict[input[x]] += 1
        else:
            newdict[input[x]] = 1
        x += 1
    return newdict


def favorite_color(input: dict[str, str]) -> str:
    color_count: list[str] = []
    newdict: dict[str, int] = {}
    mode = 0
    mode_color = ""
    for key in input:
        color_count.append(input[key])
    newdict = count(color_count)
    for key in newdict:
        if newdict[key] > mode:
            mode = newdict[key]
            mode_color = key
    return mode_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    newdict: dict[int, set[str]] = {}
    x = 0
    while x < len(words):
        if len(words[x]) not in newdict:
            newdict[len(words[x])] = set()
        if words[x] not in newdict[len(words[x])]:
            newdict[len(words[x])].add(words[x])
        x += 1
    return newdict


# return newdict
