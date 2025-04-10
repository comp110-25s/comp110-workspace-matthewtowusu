"""File to define River class."""

__author__ = """730574445"""


from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        newfish: list[Fish] = []
        newbear: list[Bear] = []
        for f in self.fish:
            if f.age <= 3:
                newfish.append(f)
            self.fish = newfish
        for b in self.bears:
            if b.age <= 5:
                newbear.append(b)
            self.bear = newbear
        return None

    def bears_eating(self):
        if len(self.fish) >= 5:
            self.remove_fish(3)
            for b in self.bears:
                b.eat(3)
        return None

    def check_hunger(self):
        alive_bears: list[Bear] = []
        for b in self.bears:
            if b.hunger_score >= 0:
                alive_bears.append(b)
                self.bear = alive_bears
        return None

    def repopulate_fish(self):
        pairs = len(self.fish) // 2
        x = 0
        while x < pairs:
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            x += 1
        return None

    def repopulate_bears(self):
        pairs = len(self.bears) // 2
        x = 0
        while x < pairs:
            self.bears.append(Bear())
            x += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)} ")
        print(f"Bear population: {len(self.bears)} ")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        x = 0
        while x < amount:
            self.fish.pop(0)
            x += 1
