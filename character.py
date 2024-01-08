import random

class Character:
    """_summary_"""

    def __init__(
        self,
        name: str = None,
        kindred: str = None,
        ability_scores: dict = None,
        ability_mods: dict = {"str": 0, "int": 0, "wis": 0, "dex": 0, "con": 0, "cha": 0},
        char_class: str = {"str": 0, "int": 0, "wis": 0, "dex": 0, "con": 0, "cha": 0},
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
        self.ability_scores["str"] = Die(6).roll_dice(3)
        self.ability_scores["int"] = Die(6).roll_dice(3)
        self.ability_scores["wis"] = Die(6).roll_dice(3)
        self.ability_scores["dex"] = Die(6).roll_dice(3)
        self.ability_scores["con"] = Die(6).roll_dice(3)
        self.ability_scores["cha"] = Die(6).roll_dice(3)

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
        if not (value%2) == 0:
            raise ValueError("Even number expected")
        self._sides = value
    
    def roll_dice(self, num_of_dice: int = 1) -> int:
        """_summary_

        Args:
            num_of_dice (int, optional): Number of dice to bel rolled. Defaults to 1.

        Returns:
            int: total number of 
        """
        #TODO: add 'self.modifier' arg to add/subtract final points from score
        self.num_of_dice = num_of_dice
        self.dice = f"{self.num_of_dice}d{self.sides}"
        print(f"Rolling {self.dice}")
        def roll_one_die():
            return random.randint(1, self.sides)
        results = []
        for num in range(0, self.num_of_dice):
            roll = roll_one_die()
            print(f"Result of roll {num}: {roll}")
            results.append(roll)
        total = sum(results)
        return total, results

grendl = Character(
    name="Grendl",
    kindred="Grimalkin",
    ability_scores={"str": 0, "int": 0, "wis": 0, "dex": 0, "con": 0, "cha": 0},
    ability_mods={"str": 0, "int": 0, "wis": 0, "dex": 0, "con": 0, "cha": 0},
    char_class="Friar",
    max_hit_points=10,
    current_hit_points=10,
)

#print(grendl)
# print(grendl.adj_current_hp(-1))
#print(grendl)
print(Die(6).roll_dice(3))