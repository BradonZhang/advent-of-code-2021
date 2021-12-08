with open('in/8.txt') as f:
    lines = f.read().splitlines()


# Part 1

total = 0
for line in lines:
    _, x = line.split(' | ')
    for y in x.split():
        if len(y) in [2, 3, 4, 7]:
            total += 1

print(total)


# Part 2

class DigitMap:
    def __init__(self, line):
        self.tokens = [set(x) for x in line.replace('| ', '').split()]
        self.digits = self.tokens[0:10]
        self.output = self.tokens[10:]
        self.digits.sort(key=lambda x: len(x))
        self.ans = [None] * 10
        self.ans[1] = self.digits[0]
        self.ans[7] = self.digits[1]
        self.ans[4] = self.digits[2]
        self.ans[8] = self.digits[9]
        self.ans[3] = [x for x in self.digits[3:6] if len(x & self.ans[1]) == 2][0]
        self.ans[2] = [x for x in self.digits[3:6] if len(x & self.ans[4]) == 2][0]
        self.ans[5] = [x for x in self.digits[3:6] if x not in self.ans][0]
        self.ans[6] = [x for x in self.digits[6:9] if len(x & self.ans[1]) == 1][0]
        self.ans[0] = [x for x in self.digits[6:9] if len(x & self.ans[5]) == 4][0]
        self.ans[9] = [x for x in self.digits[6:9] if x not in self.ans][0]
    def get_output(self):
        total = 0
        for x in self.output:
            total *= 10
            for i in range(10):
                if self.ans[i] == x:
                    total += i
                    break
        return total

total = 0
for line in lines:
    dm = DigitMap(line)
    total += dm.get_output()
print(total)
