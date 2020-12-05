import sys

sums = {}
numbers = []
for line in sys.stdin:
    numbers.append(int(line))
for num1 in numbers:
    for num2 in numbers:
        sums[2020 - (num1 + num2)] = (num1, num2)
for number in numbers:
    if number in sums:
        print number * sums[number][0] * sums[number][1]
        break
