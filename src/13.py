import numpy as np
from PIL import Image

with open('in/13.txt') as f:
    coords_text, folds_text = f.read().split('\n\n')

coords = [tuple(int(x) for x in line.split(',')) for line in coords_text.splitlines()]

grid = set(coords)

class Fold:
    def __init__(self, line):
        self.axis = int(line[11] == 'y')
        self.val = int(line[13:])

folds = map(Fold, folds_text.splitlines())
folded = False

for fold in folds:
    to_remove = set(p for p in grid if p[fold.axis] >= fold.val)

    for x, y in to_remove:
        if fold.axis:
            if fold.val * 2 >= y:
                grid.add((x, fold.val * 2 - y))
        else:
            if fold.val * 2 >= x:
                grid.add((fold.val * 2 - x, y))
        grid.remove((x, y))

    # Part 1
    if not folded:
        folded = True
        print(len(grid))


# Part 2

coords = np.array(tuple(grid))
disp = np.zeros((np.max(coords[:, 0]) + 1, np.max(coords[:, 1]) + 1), dtype=bool)
disp[tuple(np.transpose(coords))] = 1
disp = np.transpose(disp)

for row in disp:
    for cell in row:
        print('#' if cell else ' ', end='')
    print()
Image.fromarray(disp).show()
