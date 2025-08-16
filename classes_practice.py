import random

#player class
class Player:
    starting_score = 100

    def __init__(self, name):
        self.name = name
        self.score = starting_score
        self.level = 1
        self.roll = 0

    @classmethod
    def set_starting_score(cls, choice):
        if choice == 0:
            print("Standard Game Selected")
        elif choice == 1:
            print("Rapid Game Selected")
            cls.starting_score = 50
        elif choice == 2:
            print("Extended Game Selected")
            cls.starting_score = 150

    def roll_die(self):
        self.roll = random.randint(1,10)
        print(f"{self.name} rolled a {self.roll}")

    @staticmethod
    def calculate_impact(roll_one, roll_two):
        difference = abs(roll_one - roll_two)
        return difference

    def level_up(self, roll_one, roll_two):
        multiplier = 1 + (Player.calculate_impact(roll_one, roll_two) * 0.1)
        self.level = self.level * multiplier
        print(f"{self.name} has been promoted to level {self.level}!")

    def heal(self, roll_one, roll_two):
        revival = Player.calculate_impact(roll_one, roll_two) * 5 * level
        self.score = self.score + revival
        print(f"{self.name} healed {revival} points. Score: {self.score}")

    def harm(self, roll_one, roll_two):
        damage = Player.calculate_impact(roll_one, roll_two) * 5 * level
        self.score = self.score - damage
        print(f"{self.name} was attacked and lost {damage} points. Score: {self.score}")

#function that runs one round
def one_round(p1, p2):
    entry_one = input((f"{p1.name}, press x to roll the d10 die"))
    if entry_one == "x":
        p1.roll_die()
    entry_two = input((f"{p2.name}, press x to roll the d10 die"))
    if entry_two == "x":
        p2.roll_die()
    if p1.roll > p2.roll:
        print(f"{p1.name}, you won! Would you like to attack, defend, or level up?")
        move_selection_one = input("Press a to attack, d to defend, or l to level up: ")
        if move_selection_one == "a":
            p2.harm(p1.roll, p2.roll)
        elif move_selection_one == "d":
            p1.heal(p1.roll, p2.roll)
        elif move_selection_one == "l":
            p1.level_up(p1.roll, p2.roll)
    elif p2.roll > p1.roll:
        print(f"{p2.name}, you won! Would you like to attack, defend, or level up?")
        move_selection_two = input("Press a to attack, d to defend, or l to level up: ")
        if move_selection_two == "a":
            p1.harm(p1.roll, p2.roll)
        elif move_selection_two == "d":
            p2.heal(p1.roll, p2.roll)
        elif move_selection_two == "l":
            p2.level_up(p1.roll, p2.roll)
    elif p1.roll == p2.roll:
        print("It's a tie... try again.")

#code that runs the entire game




