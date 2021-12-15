import numpy as np
import heapq

with open('./in/15.txt') as f:
    grid = np.array([[int(x) for x in line] for line in f.read().splitlines()])

R, C = grid.shape
D = [(-1, 0), (0, -1), (0, 1), (1, 0)]


# Part 1

pq = [(0, 0, 0)]
lowest = {}
visited = set()

while len(pq):
    w, r, c = heapq.heappop(pq)
    if (r, c) in visited:
        continue
    if (r, c) == (R - 1, C - 1):
        break
    visited.add((r, c))
    for dr, dc in D:
        r1 = r + dr
        c1 = c + dc
        if not (0 <= r1 < R) or not (0 <= c1 < C):
            continue
        if (r1, c1) in visited:
            continue
        lowest.setdefault((r1, c1), float('inf'))
        w1 = w + grid[r1, c1]
        if w1 < lowest[r1, c1]:
            lowest[r1, c1] = w1
            heapq.heappush(pq, (w1, r1, c1))

print(lowest[R - 1, C - 1])


# Part 2

pq = [(0, 0, 0)]
lowest = {}
visited = set()

while len(pq):
    w, r, c = heapq.heappop(pq)
    if (r, c) in visited:
        continue
    if (r, c) == (R * 5 - 1, C * 5 - 1):
        break
    visited.add((r, c))
    for dr, dc in D:
        r1 = r + dr
        c1 = c + dc
        if not (0 <= r1 < R * 5) or not (0 <= c1 < C * 5):
            continue
        if (r1, c1) in visited:
            continue
        lowest.setdefault((r1, c1), float('inf'))
        w0 = grid[r1 % R, c1 % C] + r1 // R + c1 // C
        if w0 > 9:
            w0 -= 9
        w1 = w + w0
        if w1 < lowest[r1, c1]:
            lowest[r1, c1] = w1
            heapq.heappush(pq, (w1, r1, c1))

print(lowest[R * 5 - 1, C * 5 - 1])
