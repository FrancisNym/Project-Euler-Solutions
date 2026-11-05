# How many routes from top left to bottom right of a 20x20 grid

# We can solve this using just combinatorics and logic
import math


def Solution():
    return math.factorial(40) // (math.factorial(20) * math.factorial(20))

print(Solution())