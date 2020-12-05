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

hiid = -1
for bpass in sys.stdin:
    i = id(seat(bpass))
    if i > hiid:
        hiid = i
print hiid
