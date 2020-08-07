from random import seed
from random import randint  # place `import` statement at top of the program

# don't modify this code or variable `n` may not be available
n = int(input())

seed(n)

print(randint(-100, 100))
