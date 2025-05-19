import random

noOfStreaks = 0
for n in range(10000):
    flip = []
    for x in range(100):
        flip.append(random.choice(['H', 'T']))
    streak = 1
    for i in range(1,100):
        if flip[i] == flip[i-1]:
            streak += 1
            if streak == 6:
                noOfStreaks += 1
                break
        else:
            streak = 1
print('Chance of streak: %s%%' % (noOfStreaks / 100))