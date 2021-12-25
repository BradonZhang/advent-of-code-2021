import re
from functools import lru_cache

with open('in/23.txt') as f:
    order = re.findall('[A-D]', f.read())
    assert len(order) == 8

def dest(c):
    assert 'A' <= c <= 'D'
    return ord(c) - ord('A')

def energy(i):
    assert 0 <= i < 4
    return 10 ** i

def walk_cost(room_index, hall_index):
    assert room_index in range(4)
    assert hall_index in range(7)
    if hall_index in (0, 1):
        return (2 - hall_index) + 2 * room_index
    if hall_index in (5, 6):
        return (hall_index - 4) + 2 * (3 - room_index)
    if room_index < hall_index - 1:
        return 2 * (hall_index - 1 - room_index) - 1
    return 2 * (room_index - hall_index + 1) + 1

@lru_cache(maxsize=None)
def move(room_sizes, hallway, max_room_sizes):
    if room_sizes == max_room_sizes and not any(hallway):
        return 0
    best = float('inf')
    for i, room_size in enumerate(room_sizes):
        if room_size >= 0:
            continue
        c = order[4 * (room_size - len(order) // 4 + max_room_sizes[i]) + i]
        a, b = i + 1, i + 2
        for r in (range(a, -1, -1), range(b, 7)):
            for j in r:
                if hallway[j] is not None:
                    break
                new_room_sizes = tuple(room_sizes[k] + 1 if i == k else room_sizes[k] for k in range(4))
                new_hallway = tuple(c if j == k else hallway[k] for k in range(7))
                steps = walk_cost(i, j) + room_size + 1 + max_room_sizes[i]
                best = min(best, steps * energy(dest(c)) + move(new_room_sizes, new_hallway, max_room_sizes))
    for j, c in enumerate(hallway):
        if c is None:
            continue
        i = dest(c)
        if room_sizes[i] < 0:
            continue
        if any(hallway[j + 1:i + 2] + hallway[i + 2:j]):
            continue
        new_room_sizes = tuple(room_sizes[k] + 1 if i == k else room_sizes[k] for k in range(4))
        new_hallway = tuple(None if j == k else hallway[k] for k in range(7))
        steps = walk_cost(i, j) + max_room_sizes[i] - room_sizes[i]
        best = min(best, steps * energy(i) + move(new_room_sizes, new_hallway, max_room_sizes))
    return best


# Part 1
# Originally done by hand; adjusted code to let it work here

max_room_sizes = [2] * 4
for i in range(4):
    if dest(order[i + 4]) == i:
        max_room_sizes[i] -= 1
        if dest(order[i]) == i:
            max_room_sizes[i] -= 1
print(move(tuple(-x for x in max_room_sizes), (None,) * 7, tuple(max_room_sizes)))


# Part 2

fold_text = """  #D#C#B#A#
  #D#B#A#C#"""
order = order[:4] + re.findall('[A-D]', fold_text) + order[4:]
assert len(order) == 16
max_room_sizes = [4] * 4
for i in range(4):
    for j in range(3, -1, -1):
        if dest(order[i + 4 * j]) == i:
            max_room_sizes[i] -= 1
        else:
            break
print(move(tuple(-x for x in max_room_sizes), (None,) * 7, tuple(max_room_sizes)))
