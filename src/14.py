with open('in/14.txt') as f:
    lines = f.read().splitlines()
    polymer_text = lines.pop(0)
    lines.pop(0)


children = {}

for line in lines:
    children[(line[0], line[1])] = line[6]


# Part 1

class Node:
    def __init__(self, val, nxt=None) -> None:
        self.val = val
        self.next = nxt

counts = {}

head = None
tail = None
for p in polymer_text:
    if p not in counts:
        counts[p] = 0
    counts[p] += 1
    if head is None:
        head = Node(p)
        tail = head
    else:
        P = Node(p)
        tail.next = P
        tail = P

for i in range(10):
    curr = head
    while curr != tail:
        child = children.get((curr.val, curr.next.val))
        if child is None:
            continue
        if child not in counts:
            counts[child] = 0
        counts[child] += 1
        nxt = curr.next
        curr.next = Node(child, nxt)
        curr = nxt

print(max(counts.values()) - min(counts.values()))


# Part 2

counts = {}

first_pair = None
for i in range(len(polymer_text) - 1):
    pair = (polymer_text[i], polymer_text[i + 1])
    if first_pair is None:
        first_pair = pair
    if pair not in counts:
        counts[pair] = 0
    counts[pair] += 1

for i in range(40):
    fp = first_pair
    for p, c in list(counts.items()):
        child = children.get(p)
        if child is None:
            continue
        if (p[0], child) not in counts:
            counts[(p[0], child)] = 0
        if (child, p[1]) not in counts:
            counts[(child, p[1])] = 0
        counts[(p[0], child)] += c
        counts[(child, p[1])] += c
        counts[p] -= c
        if p == fp:
            first_pair = (p[0], child)

letter_counts = {}
letter_counts[first_pair[0]] = counts[first_pair]
for p, c in counts.items():
    if p[1] not in letter_counts:
        letter_counts[p[1]] = 0
    letter_counts[p[1]] += c

print(max(letter_counts.values()) - min(letter_counts.values()))
