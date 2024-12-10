import re

file = open("day3_part1.txt","r")
test_str = file.read().strip()
file.close()

regex = r"mul\((\d{1,3}),(\d{1,3})\)"

#test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

matches = re.findall(regex, test_str)

sum = 0
for match in matches:
    sum += int(match[0]) * int(match[1])

print(sum)