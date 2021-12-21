from collections import Counter
import numpy as np

with open('in/21.txt') as f:
    p0, p1 = [int(line.split()[-1]) for line in f.read().splitlines()]


# Part 1

pos = [p0, p1]
scores = [0, 0]
die = 0
player = 0
while True:
    pos[player] += 3 * (die % 100 + 1) + 3
    pos[player] %= 10
    if pos[player] == 0:
        pos[player] = 10
    scores[player] += pos[player]
    die += 3
    if scores[player] >= 1000:
        print(scores[1 - player] * die)
        break
    player = 1 - player


# Part 2

pos_count = np.array([0, 0, 0, 1, 3, 6, 7, 6, 3, 1])
pos_score = np.array([i if i > 0 else 10 for i in range(10)])

pos = [p0 % 10, p1 % 10]
scores = [0, 0]
player = 0
wins = [0, 0]
# simul[pos, score] = count
simul = [Counter([(pos[0], 0)]), Counter([(pos[1], 0)])]

while simul[0] and simul[1]:
    new_simul = Counter()
    opp_total = 0
    for c in simul[1 - player].values():
        opp_total += c
    for (p, s), c in simul[player].items():
        new_counts = c * np.roll(pos_count, p)
        new_scores = s + pos_score
        for i in range(10):
            if new_counts[i] == 0:
                continue
            if new_scores[i] >= 21:
                wins[player] += new_counts[i] * opp_total
            else:
                new_simul[(i, new_scores[i])] += new_counts[i]
    simul[player] = new_simul
    player = 1 - player

print(max(wins))
