import random

# choose a side and run the program.

toss = random.randint(0, 1)

if toss == 0:
    print("heads")
elif toss == 1:
    print("tails")