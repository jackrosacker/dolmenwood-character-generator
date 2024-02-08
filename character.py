import random


class Character:
    """_summary_"""

    def __init__(
        self,
        name: str = None,
        kindred: str = None,
        ability_scores: dict = {
            "str": 0,
            "int": 0,
            "wis": 0,
            "dex": 0,
            "con": 0,
            "cha": 0,
        },
        ability_mods: dict = {
            "str": 0,
            "int": 0,
            "wis": 0,
            "dex": 0,
            "con": 0,
            "cha": 0,
        },
        char_class: str = None,
        max_hit_points: int = None,
        current_hit_points: int = None,
        status: str = "Alive",
    ) -> None:
        self.name = name
        self.kindred = kindred
        self.ability_scores = ability_scores
        self.ability_mods = ability_mods
        self.char_class = char_class
        self.max_hit_points = max_hit_points
        self.current_hit_points = current_hit_points
        self.status = status

    def __str__(self) -> str:
        return f"Character attributes:\n \
        name: {self.name}\n \
        kindred: {self.kindred}\n \
        ability scores: {self.ability_scores}\n \
        ability mods: {self.ability_mods}\n \
        class: {self.char_class}\n \
        max hp: {self.max_hit_points}\n \
        current hp: {self.current_hit_points}\n \
        status: {self.status}"

    def adj_current_hp(self, hp_change: int):
        print(f"HP changing by {hp_change}")
        if (self.current_hit_points + hp_change) > self.max_hit_points:
            self.current_hit_points = self.max_hit_points
        else:
            self.current_hit_points = self.current_hit_points + hp_change
        if self.current_hit_points <= 0:
            self.status = "Dead"
            return f"{self.name} has {self.current_hit_points} HP. They are now dead."

    def generate_ability_scores(self):
        self.ability_scores["str"], placeholder, placeholder = Die(6).roll_dice(3)
        self.ability_scores["int"], placeholder, placeholder = Die(6).roll_dice(3)
        self.ability_scores["wis"], placeholder, placeholder = Die(6).roll_dice(3)
        self.ability_scores["dex"], placeholder, placeholder = Die(6).roll_dice(3)
        self.ability_scores["con"], placeholder, placeholder = Die(6).roll_dice(3)
        self.ability_scores["cha"], placeholder, placeholder = Die(6).roll_dice(3)


class Die:
    """Object representing a game die"""

    def __init__(self, sides: int) -> None:
        self.sides = sides

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, value):
        """limit sides of die to even numbers only"""
        if not (value % 2) == 0:
            raise ValueError("Even number expected")
        self._sides = value

    def roll_dice(self, num_of_dice: int = 1, modifier: int = 0):
        """_summary_

        Args:
            num_of_dice (int, optional): Number of dice to be rolled. Defaults to 1.
            modifier (int, optional): Value to add or subtract from sum of roll results.

        Returns:
            int: _description_
            list: _description_
            modifier: _description_
        """
        total: int
        roll_results: list[int]
        self.num_of_dice = num_of_dice
        self.dice = f"{self.num_of_dice}d{self.sides}"
        self.modifier = modifier
        print(f"Rolling {self.dice}...")
        if self.modifier != 0:
            print(f"Adding modifier {self.modifier}")

        def roll_one_die():
            return random.randint(1, self.sides)

        roll_results = []
        for num in range(0, self.num_of_dice):
            roll = roll_one_die()
            roll_results.append(roll)
        total = sum(roll_results) + self.modifier
        print(f"  roll results: {roll_results}")
        print(f"  modifier: {self.modifier}")
        print(f"  roll total: {total}")
        return total, roll_results, self.modifier
