import re

with open('in/22.txt') as f:
    lines = f.read().splitlines()

def get_command(line):
    oo, coords = line.split()
    m = re.match(r'x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', coords)
    return (oo == 'on', [int(x) for x in m.groups()])
commands = [get_command(line) for line in lines]


# Part 1

on = set()

for is_on, bounds in commands:
    x1, x2, y1, y2, z1, z2 = bounds
    for x in range(max(-50, x1), min(51, x2 + 1)):
        for y in range(max(-50, y1), min(51, y2 + 1)):
            for z in range(max(-50, z1), min(51, z2 + 1)):
                if is_on:
                    on.add((x, y, z))
                else:
                    on.discard((x, y, z))

print(len(on))


# Part 2

def intersect_ranges(r11, r12, r21, r22):
    assert r12 >= r11 and r22 >= r21
    if r21 > r12 or r11 > r22:
        return None
    nums = sorted([r11, r12, r21, r22])
    return [nums[1], nums[2]]

def intersect_bounds(bounds1, bounds2):
    x11, x12, y11, y12, z11, z12 = bounds1
    x21, x22, y21, y22, z21, z22 = bounds2
    X = intersect_ranges(x11, x12, x21, x22)
    Y = intersect_ranges(y11, y12, y21, y22)
    Z = intersect_ranges(z11, z12, z21, z22)
    if not all((X, Y, Z)):
        return None
    return X + Y + Z

class Cuboid:
    def __init__(self, bounds) -> None:
        self.bounds = bounds
        self.vacuums = []
    def remove(self, bounds):
        shaved_bounds = intersect_bounds(self.bounds, bounds)
        if not shaved_bounds:
            return
        for vacuum in self.vacuums:
            vacuum.remove(shaved_bounds)
        self.vacuums.append(Cuboid(shaved_bounds))
    def volume(self):
        x1, x2, y1, y2, z1, z2 = self.bounds
        return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) - sum(vacuum.volume() for vacuum in self.vacuums)

cuboids = []
for is_on, bounds in commands:
    for cuboid in cuboids:
        cuboid.remove(bounds)
    if is_on:
        cuboids.append(Cuboid(bounds))

print(sum(cuboid.volume() for cuboid in cuboids))
