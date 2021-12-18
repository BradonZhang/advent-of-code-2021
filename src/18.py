import math
from collections import deque
from copy import deepcopy

with open('in/18.txt') as f:
    lines = f.read().splitlines()

class Node:
    def __init__(self, arr, presimplify=True) -> None:
        self.val = arr
        if not self.is_num():
            if not isinstance(arr[0], Node):
                self.val = (Node(arr[0]), Node(arr[1]))
        if presimplify:
            self.simplify()
    def __add__(self, other):
        return Node([deepcopy(self), deepcopy(other)])
    def is_num(self):
        return type(self.val) == int
    def is_simple(self):
        return not self.is_num() and self.val[0].is_num() and self.val[1].is_num()
    def simplify(self):
        while True:
            prev_leaf = None
            next_leaf_val = None
            split_leaf = None
            all_done = False
            def explode(node, depth=0):
                nonlocal prev_leaf, next_leaf_val, split_leaf, all_done
                def done():
                    return next_leaf_val is not None
                if node.is_num():
                    if done():
                        if not all_done:
                            node.val += next_leaf_val
                            all_done = True
                        return None
                    prev_leaf = node
                    if node.val >= 10 and not split_leaf:
                        split_leaf = node
                    return None
                if done():
                    explode(node.val[0])
                    explode(node.val[1])
                    return None
                if depth >= 4 and node.is_simple():
                    temp = node.val
                    node.val = 0
                    return temp
                e1 = explode(node.val[0], depth + 1)
                if e1 and not done():
                    if prev_leaf:
                        prev_leaf.val += e1[0].val
                    next_leaf_val = e1[1].val
                e2 = explode(node.val[1], depth + 1)
                if e2 and not done():
                    if prev_leaf:
                        prev_leaf.val += e2[0].val
                    next_leaf_val = e2[1].val
                return None
            explode(self)

            if next_leaf_val is not None:
                continue
            if split_leaf:
                x = split_leaf.val
                split_leaf.val = (Node(math.floor(x / 2), False), Node(math.ceil(x / 2), False))
                continue
            break
    def mag(self):
        if self.is_num():
            return self.val
        return 3 * self.val[0].mag() + 2 * self.val[1].mag()
    def list(self):
        if self.is_num():
            return self.val
        return [self.val[0].list(), self.val[1].list()]
    def __str__(self):
        return str(self.list())

nodes = [Node(eval(line)) for line in lines]


# Part 1

print(sum(nodes[1:], nodes[0]).mag())


# Part 2

best = 0
for u in nodes:
    for v in nodes:
        if u == v:
            continue
        best = max(best, (u + v).mag())
print(best)
