import numpy as np
import math

with open('in/2.txt') as f:
    tokens = [x.split() for x in f.readlines()]

# Part 1
dirs = {
    'forward': np.array([1, 0]),
    'up': np.array([0, -1]),
    'down': np.array([0, 1]),
}

vecs = [dirs[direction] * int(amount) for direction, amount in tokens]
print(math.prod(sum(vecs)))

# Part 2
aim = 0
x = 0
d = 0
for direction, amount in tokens:
    X = int(amount)
    if direction == 'down':
        aim += X
    elif direction == 'up':
        aim -= X
    else:
        x += X
        d += aim * X
print(x * d)
