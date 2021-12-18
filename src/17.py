import math
import re


with open('in/17.txt') as f:
    m = re.match(r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)', f.read().strip())
    min_x, max_x, min_y, max_y = (int(x) for x in m.groups())

assert 0 <= min_x <= max_x and min_y <= max_y < 0

def tri(x):
    return x * (x + 1) // 2

def inv_tri(y):
    return (-1 + math.sqrt(1 + 8 * y)) / 2


# Part 1

max_dy = -min_y - 1
print(max_dy)


# Part 2

def ranges_intersect(x0, x1, y0, y1):
    assert x0 <= x1 and y0 <= y1
    return not (x0 > y1 or x1 < y0)

x_steps = []
for dx in range(math.ceil(inv_tri(min_x)), max_x + 1):
    min_steps = None
    max_steps = float('inf')
    dxx = dx
    x = 0
    steps = 0
    while dxx:
        x += dxx
        dxx -= 1
        if x > max_x:
            max_steps = steps
            break
        steps += 1
        if x >= min_x and min_steps is None:
            min_steps = steps
    if min_steps is None:
        continue
    x_steps.append((min_steps, max_steps))

y_steps = []
for dy in range(min_y, max_dy + 1):
    min_steps = None
    max_steps = None
    dyy = dy
    y = 0
    steps = 0
    while True:
        y += dyy
        dyy -= 1
        if min_y > y:
            max_steps = steps
            break
        steps += 1
        if min_y <= y <= max_y and min_steps is None:
            min_steps = steps
    if min_steps is None:
        continue
    y_steps.append((min_steps, max_steps))


total = 0
for x0, x1 in x_steps:
    for y0, y1 in y_steps:
        total += ranges_intersect(x0, x1, y0, y1)
print(total)
