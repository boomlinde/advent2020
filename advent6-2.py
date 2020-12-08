import sys

def mask(char):
    return 1 << (ord(char) - ord('a'))

def nbits(n):
    s = 0
    while n:
        s += n & 1
        n >>= 1
    return s

groups = [0xffffffff]
for line in sys.stdin:
    if line == '\n':
        groups.append(0xffffffff)
        continue
    groups[-1] &= sum(mask(q) for q in line.strip())


print sum(nbits(g) for g in groups)
