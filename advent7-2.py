import sys
import re

def parse(line):
    m = re.match(r'^(.+) bags contain (.+)$', line)
    name = m.group(1)

    content = {}
    for item in  m.group(2).split(', '):
        if item == 'no other bags.':
            continue
        m = re.match(r'^(\d+) ([a-z ]+) bags?.?', item)
        content[m.group(2)] = int(m.group(1))

    return (name, content)

def count(r, color):
    return sum(c + c * count(r, ch) for ch, c in r[color].items())

rules = {}
for line in sys.stdin:
    rules.update(dict([parse(line.strip())]))

print count(rules, 'shiny gold')
