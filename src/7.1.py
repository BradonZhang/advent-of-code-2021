with open('in/7.txt') as f:
    pos = [int(x) for x in f.read().split(',')]

a = min(pos)
b = max(pos)


# Part 1

best = float('inf')
for i in range(a, b + 1):
    best = min(best, sum(abs(p - i) for p in pos))
print(best)


# Part 2

best = float('inf')
for i in range(a, b + 1):
    best = min(best, sum((d := abs(p - i)) * (d + 1) // 2 for p in pos))
print(best)
