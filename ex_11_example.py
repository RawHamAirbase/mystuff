import re
fhand = open("regex_sum_42.txt")
tot = 0
for line in fhand:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    for val in num:
        tot += int(val)
print(tot)
