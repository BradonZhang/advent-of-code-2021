import numpy as np

with open('in/5.txt') as f:
    lines = f.read().splitlines()


# Part 1

coords = [tuple(int(x) for x in line.replace(' -> ', ',').split(',')) for line in lines]
hori = [(x1, y1, x2, y2) for x1, y1, x2, y2 in coords if y1 == y2]
vert = [(x1, y1, x2, y2) for x1, y1, x2, y2 in coords if x1 == x2]
n = 0
for x1, y1, x2, y2 in coords:
    n = max(n, x1, y1, x2, y2)
n += 1
grid = np.zeros((n, n))
for x1, y1, x2, y2 in hori:
    if x1 > x2:
        x2, x1 = x1, x2
    for x in range(x1, x2 + 1):
        grid[x, y1] += 1
for x1, y1, x2, y2 in vert:
    if y1 > y2:
        y2, y1 = y1, y2
    for y in range(y1, y2 + 1):
        grid[x1, y] += 1

print(np.count_nonzero(grid > 1))


# Part 2

grid = np.zeros((n, n))
for x1, y1, x2, y2 in coords:
    dx = 0
    if x2 > x1:
        dx = 1
    if x1 > x2:
        dx = -1
        
    dy = 0
    if y2 > y1:
        dy = 1
    if y1 > y2:
        dy = -1
        
    x = x1
    y = y1

    grid[x, y] += 1
    while x != x2 or y != y2:
        x += dx
        y += dy
        try:
            grid[x, y] += 1
        except:
            print((x1, y1, x2, y2, x, y))

print(np.count_nonzero(grid > 1))
