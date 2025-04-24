#rolldice
import random

    
side = 6
die1 : int = random.randint(1, side)
die2: int = random.randint(1, side)
total: int= die1+ die2
print("First die:", die1)
print("Second die:", die2)
print("Total of two dice:", total)
