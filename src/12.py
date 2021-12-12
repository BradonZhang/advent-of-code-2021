with open('in/12.txt') as f:
    lines = f.read().splitlines()

edges = [line.split('-') for line in lines]
adj_list = {}
for a, b in edges:
    adj_list.setdefault(a, set()).add(b)
    adj_list.setdefault(b, set()).add(a)

def is_big(node):
    return node.upper() == node


# Part 1

visited = set()
def count_paths(node: str):
    if node == 'end':
        return 1
    if not is_big(node):
        visited.add(node)
    total = 0
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            total += count_paths(neighbor)
    if not is_big(node):
        visited.remove(node)
    return total

print(count_paths('start'))


# Part 2

visited = set()
doubled = None
def count_paths2(node: str):
    global doubled
    if node == 'end':
        return 1
    if not is_big(node):
        visited.add(node)
    total = 0
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            total += count_paths2(neighbor)
        elif doubled is None and neighbor != 'start':
            doubled = neighbor
            total += count_paths2(neighbor)
    if not is_big(node):
        if doubled == node:
            doubled = None
        else:
            visited.remove(node)
    return total

print(count_paths2('start'))
