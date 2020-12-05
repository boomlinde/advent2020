import sys

def walk(syms, rang, path):
    l, u = rang
    if not path:
        return l
    if path[0] == syms[0]:
        u = (u + l) / 2
    else:
        l = (u + l) / 2
    return walk(syms, (l, u), path[1:])


def seat(path):
    return (
        walk('FB', (0, 128), path[:7]),
        walk('LR', (0, 8), path[7:]),
    )

def id(seat):
    return seat[0] * 8 + seat[1]

taken = set()
for bpass in sys.stdin:
    taken.add(id(seat(bpass)))

lastoccupied = False
for i in range(0, (1 << (3 + 7))):
    if lastoccupied and not i in taken:
        break
    lastoccupied = i in taken
print i
