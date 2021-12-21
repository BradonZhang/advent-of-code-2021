from collections import deque, defaultdict
import numpy as np

matrices = []
for a in range(6):
    i = a % 3
    isign = 1 - 2 * (a >= 3)
    for b in range(4):
        j = b % 2
        j += j >= i
        jsign = 1 - 2 * (b >= 2)
        k = [x for x in range(3) if x not in [i, j]][0]
        ksign = isign * jsign * (2 * ((i - j + 1) % 3 == 0) - 1)
        mat = np.zeros((3, 3), dtype=int)
        mat[0][i] = isign
        mat[1][j] = jsign
        mat[2][k] = ksign
        matrices.append(mat)

class Scanner:
    def __init__(self, chunk) -> None:
        header, *lines = chunk.splitlines()
        self.num = int(header.split()[2])
        self.beacons = [np.array([int(x) for x in line.split(',')]) for line in lines]
        self.orientations = [[matrix @ beacon for beacon in self.beacons] for matrix in matrices]
        self.absolute = None
        self.pos = None

with open('in/19.txt') as f:
    scanners = [Scanner(chunk) for chunk in f.read().strip().split('\n\n')]

beacons = set()

scanners[0].absolute = scanners[0].beacons
scanners[0].pos = np.zeros(3)
q = deque([scanners[0]])
while q:
    s1 = q.popleft()
    beacons |= set(tuple(x) for x in s1.absolute)
    for s2 in scanners:
        if s2.absolute is not None:
            continue
        o1 = s1.absolute
        for o2 in s2.orientations:
            dist = defaultdict(list)
            for i, u in enumerate(o1):
                for j, v in enumerate(o2):
                    dist[tuple(u - v)].append((i, j))
            best_d = None
            for d, pairs in dist.items():
                if len(pairs) < 12:
                    continue
                p1 = set(u for u, v in pairs)
                p2 = set(v for u, v in pairs)
                if len(p1) < 12 or len(p2) < 12:
                    continue
                break
            else:
                continue
            dv = np.array(d)
            s2.absolute = [v + dv for v in o2]
            s2.pos = dv
            q.append(s2)

assert sum(scanner.absolute is not None for scanner in scanners) == len(scanners)
assert sum(scanner.pos is not None for scanner in scanners) == len(scanners)

# Part 1
print(len(beacons))


# Part 2

max_dist = 0
for s1 in scanners:
    for s2 in scanners:
        if s1 == s2:
            continue
        max_dist = max(max_dist, sum(abs(s1.pos - s2.pos)))
print(max_dist)
