import random

#player class
class Player:
    starting_score = 100

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.roll = 0

    def set_score(self, choice):
        if choice == "a":
            print("Standard Game Selected")
            self.score = 100
        elif choice == "b":
            print("Rapid Game Selected")
            self.score = 50
        elif choice == "c":
            print("Extended Game Selected")
            self.score = 150

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
        revival = Player.calculate_impact(roll_one, roll_two) * 5 * self.level
        self.score = self.score + revival
        print(f"{self.name} healed {revival} points.")

    def harm(self, roll_one, roll_two):
        damage = Player.calculate_impact(roll_one, roll_two) * 5 * self.level
        self.score = self.score - damage
        print(f"{self.name} was attacked and lost {damage} points.")

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
print("Welcome, brave warriors, to a duel to the death!")
name_one = input("Player one, enter your name: ")
p1 = Player(name_one)
name_two = input("Player two, enter your name: ")
p2 = Player(name_two)
print("Click a for standard game, b for rapid mode, and c for extended mode")
choice_one = input("Select your desired game length: ")
p1.set_score(choice_one)
p2.set_score(choice_one)
print(f"{p1.name} and {p2.name}, GET READY TO RUMBLE!!!")
while p1.score > 0 and p2.score > 0:
    one_round(p1, p2)
    print (f"{p1.name} score: {p1.score}")
    print (f"{p2.name} score: {p2.score}")
    quitting_input = input("Press q to exit the game...")
    if quitting_input == "q":
        break
if p1.score > p2.score:
    print(f"{p1.name} wins!")
elif p2.score > p1.score:
    print(f"{p2.name} wins!")
elif p1.score == p2.score:
    print("Mutually assured destruction! It is a draw!")



