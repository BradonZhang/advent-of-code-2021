from collections import deque
from statistics import median

with open('in/10.txt') as f:
    lines = f.read().splitlines()

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


# Part 1

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

total = 0
for line in lines:
    s = deque()
    for c in line:
        if c in pairs:
            s.append(c)
        else:
            if len(s) == 0 or pairs[s[-1]] != c:
                total += points[c]
                break
            s.pop()

print(total)


# Part 2

points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
scores = []
for line in lines:
    s = deque()
    for c in line:
        if c in pairs:
            s.append(c)
        else:
            if len(s) == 0 or pairs[s[-1]] != c:
                break
            s.pop()
    else:
        score = 0
        while len(s):
            curr = s.pop()
            score *= 5
            score += points[curr]
        scores.append(score)

print(median(scores))
