with open('in/20.txt') as f:
    en, init_grid = f.read().split('\n\n')
    init_grid = init_grid.splitlines()

lit = set()
min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0
for x, row in enumerate(init_grid):
    for y, cell in enumerate(row):
        if cell == '#':
            lit.add((x, y))
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

outer = '.'
for t in range(50):
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1
    new_lit = set(lit)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            index = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    oob = not (min_x < x + dx < max_x) or not (min_y < y + dy < max_y)
                    index <<= 1
                    index |= (x + dx, y + dy) in lit or (oob and outer == '#')
            if en[index] == '#':
                new_lit.add((x, y))
            else:
                new_lit.discard((x, y))
    outer = en[-1 if outer == '#' else 0]
    lit = new_lit
    # Part 1
    if t == 1:
        print(len(lit))

# Part 2
print(len(lit))
