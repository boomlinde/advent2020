import sys

def ok(char, password, index):
    if index - 1 < len(password):
        return password[index - 1] == char
    return False

def valid(line):
    policy, password = [x.strip() for x in line.split(':')]
    rang, char = policy.split(' ')
    lo, hi = [int(x) for x in rang.split('-')]
    return ok(char, password, lo) != ok(char, password, hi)

print sum(int(valid(line)) for line in sys.stdin)
