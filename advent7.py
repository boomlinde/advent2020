import sys
import re

def parse(line):
    m = re.match(r'^(.+) bags contain (.+)$', line)
    name = m.group(1)

    out = []
    for item in  m.group(2).split(', '):
        if item == 'no other bags.':
            continue
        m = re.match(r'^(\d+) ([a-z ]+) bags?.?', item)
        out.append((m.group(2), name))
    return out

def find(color, rules, found=None):
    if found is None:
        found = set()
    for parent in rules.get(color, ()):
        found.add(parent)
        find(parent, rules, found)
    return found

rules = {}
for line in sys.stdin:
    for contained, container in parse(line.strip()):
        rules[contained] = rules.get(contained, ()) + (container,)

print len(find('shiny gold', rules))
