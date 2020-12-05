import sys

def parse(inp):
    records = [{}]
    for line in inp.strip().split('\n'):
        if line == '':
            records.append({})
        records[-1].update(dict(field.split(':') for field in line.split()))
    return records

def valid(record):
    for required in 'byr iyr eyr hgt hcl ecl pid'.split():
        if required not in record:
            return False
    return True

nvalid = 0
for record in parse(sys.stdin.read()):
    nvalid += int(valid(record))
print nvalid
