import math
from collections import deque
import numpy as np

with open('in/9.txt') as f:
    grid = np.array([[int(x) for x in line] for line in f.read().strip().splitlines()])


# Part 1

R, C = len(grid), len(grid[0])

low_points = []
total = 0
D = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for r in range(R):
    for c in range(C):
        p = grid[r, c]
        for dx, dy in D:
            if not (0 <= r + dx < R) or not (0 <= c + dy < C):
                continue
            if grid[r + dx][c + dy] <= p:
                break
        else:
            low_points.append((r, c))
            total += p + 1
print(total)


# Part 2

visited = set()
basin_sizes = []
for lr, lc in low_points:
    basin_sizes.append(0)
    q = deque([(lr, lc)])
    visited.add((lr, lc))
    while len(q):
        basin_sizes[-1] += 1
        r1, c1 = q.popleft()
        for dx, dy in D:
            r2 = r1 + dx
            c2 = c1 + dy
            if not (0 <= r2 < R) or not (0 <= c2 < C):
                continue
            if (r2, c2) in visited:
                continue
            if grid[r2, c2] == 9:
                continue
            if grid[r2, c2] > grid[r1, c1]:
                q.append((r2, c2))
                visited.add((r2, c2))

basin_sizes.sort()
print(math.prod(basin_sizes[-3:]))
