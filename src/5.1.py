import numpy as np

class Line:
    def __init__(self, input_line):
        self.x1, self.y1, self.x2, self.y2 = [int(x) for x in input_line.replace(' -> ', ',').split(',')]
    def add(self, grid):
        dx = np.sign(self.x2 - self.x1)
        dy = np.sign(self.y2 - self.y1)
        x = self.x1
        y = self.y1
        grid[x, y] += 1
        while x != self.x2 or y != self.y2:
            x += dx
            y += dy
            grid[x, y] += 1
    def orth(self):
        return self.x1 == self.x2 or self.y1 == self.y2
    def max(self):
        return max(self.x1, self.x2, self.y1, self.y2)

with open('in/5.txt') as f:
    lines = [Line(line) for line in f.read().splitlines()]

n = 1 + max(line.max() for line in lines)


# Part 1

grid = np.zeros((n, n))
for line in lines:
    if line.orth():
        line.add(grid)
print(np.count_nonzero(grid > 1))


# Part 2

grid = np.zeros((n, n))
for line in lines:
    line.add(grid)
print(np.count_nonzero(grid > 1))
