with open('in/7.txt') as f:
    pos = [int(x) for x in f.read().split(',')]

a = min(pos)
b = max(pos)

# Part 1
print(min(sum(abs(p - i) for p in pos) for i in range(a, b + 1)))

# Part 2
print(min(sum((d := abs(p - i)) * (d + 1) // 2 for p in pos) for i in range(a, b + 1)))
