import re
from functools import lru_cache

with open('in/24.txt') as f:
    ftext = f.read()
    A = map(int, re.findall(r'div z (\d+)', ftext))
    B = map(int, re.findall(r'add x (-?\d+)', ftext))
    C = map(int, re.findall(r'w\nadd y (\d+)', ftext))
    args_list = list(zip(A, B, C))

# Manually decompiled from input file
def step_z(index: int, w: int, z: int):
    assert 1 <= w <= 9
    assert z >= 0
    a, b, c = args_list[index]
    x = (z % 26 + b) != w
    z //= a
    z *= 25 * x + 1
    z += (w + c) * x
    return z

@lru_cache(maxsize=None)
def deduce_w(index: int, z: int, largest: bool):
    r = range(9, 0, -1) if largest else range(1, 10)
    for w in r:
        next_z = step_z(index, w, z)
        if index == 13:
            if next_z == 0:
                return w
            continue
        if deduce_w(index + 1, next_z, largest) is not None:
            return w
    return None

# Part 1
z = 0
monad = []
for i in range(14):
    monad.append(deduce_w(i, z, True))
    z = step_z(i, monad[-1], z)
assert z == 0, z
print(''.join(map(str, monad)))

# Part 2
# Takes a while to run
z = 0
monad = []
for i in range(14):
    monad.append(deduce_w(i, z, False))
    z = step_z(i, monad[-1], z)
assert z == 0, z
print(''.join(map(str, monad)))
