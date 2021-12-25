with open('in/25.txt') as f:
    grid = [list(line) for line in f.read().splitlines()]

R, C = len(grid), len(grid[0])


# Part 1

t = 0
while True:
    t += 1

    to_clear = set()
    to_add = set()
    go_down = set()
    for r in range(R):
        for c in range(C):
            x = grid[r][c]
            if x == '.':
                continue
            if x == '>':
                if grid[r][(c + 1) % C] == '.':
                    to_clear.add((r, c))
                    to_add.add((r, (c + 1) % C))
                continue
            assert x == 'v'
            go_down.add((r, c))
    
    for r, c in to_clear:
        grid[r][c] = '.'
    for r, c in to_add:
        grid[r][c] = '>'
    moved = len(to_add)

    to_clear.clear()
    to_add.clear()
    for r, c in go_down:
        if grid[(r + 1) % R][c] == '.':
            to_clear.add((r, c))
            to_add.add(((r + 1) % R, c))
    
    for r, c in to_clear:
        grid[r][c] = '.'
    for r, c in to_add:
        grid[r][c] = 'v'
    moved += len(to_add)

    if not moved:
        print(t)
        break


# Part 2
print('Claim the second star!')
