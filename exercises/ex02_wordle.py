__author__ = """730574445"""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# Definition of the emojis used


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    x = 0
    winner = False
    while x < 6:
        print(f"=== Turn {x+1}/6 ===")
        answer = input_guess(
            len(secret)
        )  # calls the input function so that the users answer is a length the same as the secret word
        print(emojified(answer, secret))
        if answer == secret:
            print(
                f"You won in {x+1}/6 turns!"
            )  # prints the winning text, using the while loop to determine the turn
            winner = True
            x = 6
        x += 1  # counter ticks up for every turn
    if (
        winner is False
    ):  # makes sure the loosing message only pops up if the user did not finish the game
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, key_letter: str) -> bool:
    """checks the word letter by letter to see if it matches the key letter"""
    x = 0
    assert len(key_letter) == 1, f"len('{key_letter}') is not 1"
    while len(word) > x:
        if word[x] == key_letter:
            return True
        x = x + 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """checks if the letters of the guessed word contains letters with the secret word, and displays a colored square corresponding with this"""
    x = 0
    emoji: str = ""
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    while len(guess) > x:
        if secret_word[x] == guess[x]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret_word, guess[x]) is True:
                emoji += YELLOW_BOX  # calls on the contains char function and places a yellow square
            else:
                emoji += WHITE_BOX  # loads the string with a white box if the previous functions fail
        x = x + 1
    return emoji


def input_guess(num_char: int) -> str:
    counter = 0
    x = input(f"Enter a {num_char} character word:")
    while counter < 1:
        if len(x) != num_char:
            x = input(f"That wasn't {num_char} chars! Try again:")
        else:
            counter = counter + 1
    return x


if __name__ == "__main__":
    main(secret="codes")
