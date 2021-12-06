with open('in/6.txt') as f:
    fish = [int(x) for x in f.read().split(',')]
    fish2 = [x for x in fish]


# Part 1

for i in range(80):
    to_append = []
    for j, f in enumerate(fish):
        fish[j] -= 1
        if fish[j] == -1:
            to_append.append(8)
            fish[j] = 6
    fish += to_append

print(len(fish))


# Part 2

fish = fish2
counts = [0] * 7
extra = [0] * 7
curr = 0
for f in fish:
    counts[f] += 1
for i in range(256):
    extra[(curr + 2) % 7] += counts[curr]
    counts[curr] += extra[curr]
    extra[curr] = 0
    curr += 1
    curr %= 7
print(sum(counts) + sum(extra))
