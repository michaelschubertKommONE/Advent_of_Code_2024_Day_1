import re

file = open("day3_part2.txt","r")
test_str = file.read().strip()
file.close()

regex = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"

matches = re.findall(regex, test_str)

sum = 0
enable_mul = True
for match in matches:
    if match[3] == "don't()":
        enable_mul = False
    elif match[2] == "do()":
        enable_mul = True    
    elif (enable_mul and match[0] != ""):
        sum += int(match[0]) * int(match[1])

print(sum)