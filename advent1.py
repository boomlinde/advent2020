import sys

sums = {}
for number in sys.stdin:
    number = int(number)
    if number in sums:
        print sums[number] * number
        break
    sums[2020 - number] = number
