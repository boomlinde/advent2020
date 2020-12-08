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

def peek(s):
    item = s.pop()
    s.add(item)
    return item

def visit(graph, node, unmarked, tempmarks, out):
    if node not in unmarked:
        return
    if node in tempmarks:
        raise ValueError("cycle")

    tempmarks.add(node)
    for child in graph[node].keys():
        visit(graph, child, unmarked, tempmarks, out)
    tempmarks.remove(node)

    unmarked.remove(node)
    out.append((node, graph[node]))

def toposort(graph):
    unmarked = set(graph.keys())
    out = []
    while unmarked:
        visit(graph, peek(unmarked), unmarked, set(), out)
    return out

rules = {}
for line in sys.stdin:
    rules.update(dict([parse(line.strip())]))

bags = set()
for bag, content in toposort(rules):
    for other in content.keys():
        if other in bags or other == 'shiny gold':
            bags.add(bag)

print len(bags)
