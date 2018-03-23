with open("day19input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
#content = [x.strip() for x in content]

for cell_index in range(len(content[0])):
    if content[0][cell_index] == "|":
        start_index = cell_index


def set_new_dir(y, x, moving):
    #print(y, ":", x)
    if content[y][x + 1] == "-" and moving != "left":
        return "right"
    elif content[y][x - 1] == "-" and moving != "right":
        return "left"
    elif content[y - 1][x] == "|" and moving != "down":
        return "up"
    elif content[y + 1][x] == "|" and moving != "up":
        return "down"


x = start_index
y = 0
moving = "down"
result = ""
counter = 0
while True:
    counter += 1
    if moving == "down":
        y += 1
        if content[y][x].isalpha():
            result += content[y][x]
        if content[y][x] == "+":
            moving = set_new_dir(y, x, moving)
        if content[y][x] == " ":
            break
    elif moving == "left":
        x -= 1
        if content[y][x].isalpha():
            result += content[y][x]
        if content[y][x] == "+":
            moving = set_new_dir(y, x, moving)
        if content[y][x] == " ":
            break
    elif moving == "right":
        x += 1
        if content[y][x].isalpha():
            result += content[y][x]
        if content[y][x] == "+":
            moving = set_new_dir(y, x, moving)
        if content[y][x] == " ":
            break
    elif moving == "up":
        y -= 1
        # print(y, ":", x)
        if content[y][x].isalpha():
            result += content[y][x]
        if content[y][x] == "+":
            moving = set_new_dir(y, x, moving)
        if content[y][x] == " ":
            break
print(result)

# Part 2
print(counter)
