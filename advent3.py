import sys

class plane:
    def __init__(self, inp):
        self.w = len(inp.split('\n', 1)[0])
        self.data = [x for x in inp if x in '#.']
        self.h = len(self.data) / self.w
    def get(self, x, y): return self.data[(x % self.w) + y * self.w]

p = plane(sys.stdin.read())
x, y = (0, 0)
ntrees = 0
while y < p.h - 1:
    x += 3
    y += 1
    ntrees += int(p.get(x, y) == '#')
print ntrees
