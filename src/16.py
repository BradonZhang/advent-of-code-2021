from collections import deque
import math

with open('in/16.txt') as f:
    bin_str = format(int(f.read(), 16), 'b')
    bin_str = '0' * ((4 - len(bin_str)) % 4) + bin_str
    stream = deque(int(x) for x in bin_str)

class Packet:
    def __init__(self, version, packtype, val=None, subpacks=[]) -> None:
        self.version = version
        self.packtype = packtype
        self.val = val
        self.subpacks = subpacks
    def sum_versions(self):
        return self.version + sum(subpack.sum_versions() for subpack in self.subpacks)
    def eval(self):
        return [
            sum,
            math.prod,
            min,
            max,
            lambda _: self.val,
            lambda a: int(a[0] > a[1]),
            lambda a: int(a[0] < a[1]),
            lambda a: int(a[0] == a[1])
        ][self.packtype]([subpack.eval() for subpack in self.subpacks])

def read_int(stream: deque, num_bits: int):
    x = 0
    for _ in range(num_bits):
        x <<= 1
        x |= stream.popleft()
    return x

def make_packet(stream: deque):
    version = read_int(stream, 3)
    packtype = read_int(stream, 3)
    if packtype == 4:
        val = 0
        while True:
            last = not read_int(stream, 1)
            val <<= 4
            val |= read_int(stream, 4)
            if last:
                break
        return Packet(version, packtype, val)
    lentype = read_int(stream, 1)
    subpacks = []
    if lentype:
        num_packs = read_int(stream, 11)
        for _ in range(num_packs):
            subpacks.append(make_packet(stream))
    else:
        bit_len = read_int(stream, 15)
        substream = deque()
        for _ in range(bit_len):
            substream.append(stream.popleft())
        while substream:
            subpacks.append(make_packet(substream))
    return Packet(version, packtype, subpacks=subpacks)

packet = make_packet(stream)

# Part 1
print(packet.sum_versions())

# Part 2
print(packet.eval())
