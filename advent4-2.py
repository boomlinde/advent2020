import sys
import re

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

    def m(name, pattern):
        return re.match(pattern, record[name]) is not None

    return all([
        m('byr', '(19[2-9][0-9]|200[0-2])$'),
        m('iyr', '(201[0-9]|2020)$'),
        m('eyr', '(202[0-9]|2030)$'),
        m('hgt', '((1[5-8][0-9]|19[0-3])cm|([5-6][0-9]|7[0-6])in)$'),
        m('hcl', '#[0-9a-f]{6}$'),
        m('ecl', '(amb|blu|brn|gry|grn|hzl|oth)$'),
        m('pid', '[0-9]{9}$'),
    ])

nvalid = 0
for record in parse(sys.stdin.read()):
    nvalid += int(valid(record))
print nvalid
