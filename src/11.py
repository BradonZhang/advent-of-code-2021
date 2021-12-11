import numpy as np
from collections import deque
from copy import deepcopy

with open('in/11.txt') as f:
    grid = np.array([[int(x) for x in line] for line in f.read().splitlines()])
    grid2 = deepcopy(grid)

W, H = grid.shape
D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
total = 0
for i in range(100):
    grid += 1
    X, Y = np.where(grid == 10)
    free = np.ones(grid.shape)
    free[X, Y] = 0
    while len(X):
        for x, y in zip(X, Y):
            q = deque([(x, y)])
            while len(q):
                x1, y1 = q.pop()
                for dx, dy in D:
                    x2, y2 = x1 + dx, y1 + dy
                    if not (0 <= x2 < W) or not (0 <= y2 < H):
                        continue
                    grid[x2, y2] += 1
                    if grid[x2, y2] >= 10 and free[x2, y2]:
                        q.appendleft((x2, y2))
                        free[x2, y2] = 0
        X, Y = np.where(np.logical_and(grid == 10, free))
    total += np.count_nonzero(1 - free)
    grid[np.where(grid >= 10)] = 0
print(total)

grid = grid2
i = 0
while True:
    i += 1
    grid += 1
    X, Y = np.where(grid == 10)
    free = np.ones(grid.shape)
    free[X, Y] = 0
    while len(X):
        for x, y in zip(X, Y):
            q = deque([(x, y)])
            while len(q):
                x1, y1 = q.pop()
                for dx, dy in D:
                    x2, y2 = x1 + dx, y1 + dy
                    if not (0 <= x2 < W) or not (0 <= y2 < H):
                        continue
                    grid[x2, y2] += 1
                    if grid[x2, y2] >= 10 and free[x2, y2]:
                        q.appendleft((x2, y2))
                        free[x2, y2] = 0
        X, Y = np.where(np.logical_and(grid == 10, free))
    d = np.count_nonzero(1 - free)
    if d == W * H:
        print(i)
        break
    grid[np.where(grid >= 10)] = 0
    