import random

num_sides = 6
def roll_dice():
        die1: int = random.randint(1, num_sides)
        die2: int = random.randint(1, num_sides )
        total: int = die1 + die2
        print(f"the total of two dice : {total}")

def main():
            die1: int = 10
            print(f" die1 in main() start as {die1}")
            roll_dice()
            roll_dice()
            roll_dice()
            print(f" die1 in main() start as {die1}")

if __name__ == '__main__':
    main()