file = open("day4_part2.txt","r")
#test_str = file.read().strip()

matrix = []

for line in file:
    x_axis = []
    for char in line.strip():
        x_axis += [char]
    matrix += [x_axis]

file.close()

#print(matrix)

def matches_in_matrix(x, y, char):
    if y >= 0 and y < len(matrix):
        line = matrix[y]
        if x >= 0 and x < len(line):
            return line[x] == char
    return False

# In eine durch dir_x/y definierte Richtung probieren, ob die Zeichenfolge enthalten ist
def test_array(x, y, dir_x, dir_y, test_chars):
    for char in test_chars:
        if not matches_in_matrix(x, y, char):
            return False
        x += dir_x
        y += dir_y
    return True

matches = 0

for (y,line) in enumerate(matrix):
    for (x,char) in enumerate(line):
        print(f"{y}x{x} {char}")
        if char == 'A':
            if (test_array(x-1, y-1, 1, 1, "MAS") or test_array(x-1, y-1, 1, 1, "SAM")) and (test_array(x+1, y-1, -1, 1, "MAS") or test_array(x+1, y-1, -1, 1, "SAM")):
                matches += 1

print(matches)
