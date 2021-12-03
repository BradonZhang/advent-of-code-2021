with open('in/3.txt') as f:
    lines = f.read().strip().splitlines()

def gen_int(iter):
    return int(''.join(iter), 2)

# Part 1
n = len(lines[0])
counts = [0] * n
for line in lines:
    for i, c in enumerate(line):
        if c == '1':
            counts[i] += 1
        else:
            counts[i] -= 1

x = gen_int('1' if count > 0 else '0' for count in counts)
y = gen_int('0' if count > 0 else '1' for count in counts)
print(x * y)

# Part 2
o2 = [x for x in lines]
co2 = [x for x in lines]

i = 0
while len(o2) > 1:
    ones = [x for x in o2 if x[i] == '1']
    zeros = [x for x in o2 if x[i] == '0']
    o2 = zeros if len(zeros) > len(ones) else ones
    i = (i + 1) % n

i = 0
while len(co2) > 1:
    ones = [x for x in co2 if x[i] == '1']
    zeros = [x for x in co2 if x[i] == '0']
    co2 = ones if len(ones) < len(zeros) else zeros
    i = (i + 1) % n

x = gen_int(o2)
y = gen_int(co2)
print(x * y)
