import random

numberofStreaks = 0

heads = []
tails = []

for experimentNumber in range(10000):
    for i in range(100):
        coinFlip = random.randint(0,1)
        if coinFlip == 0:
            heads.append('H')
        elif coinFlip == 1:
            tails.append('T')

# code that checks if there is a streak of 6 


