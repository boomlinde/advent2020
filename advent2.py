import sys

def valid(line):
    policy, password = [x.strip() for x in line.split(':')]
    rang, char = policy.split(' ')
    lo, hi = [int(x) for x in rang.split('-')]
    nchar = len([x for x in password if x == char])
    return nchar >= lo and nchar <= hi

print sum(int(valid(line)) for line in sys.stdin)
