with open("day11input.txt") as f:
    content = f.read()

content = content.split(',')

x = 0
y = 0
# pt 2
max_dist = 0
for direction in content:
    if direction == "nw":
        y -= 1
        x -= 1
    elif direction == "n":
        y -= 2
    elif direction == "ne":
        y -= 1
        x += 1
    elif direction == "se":
        y += 1
        x += 1
    elif direction == "s":
        y += 2
    elif direction == "sw":
        y += 1
        x -= 1
    dist = (abs(min(x, y)) + (abs(x) - abs(y)) / 2)
    if dist > max_dist:
        max_dist = dist
print(x, y)
# Answer pt 1
print(abs(min(x, y)) + (abs(x) - abs(y)) / 2)
# pt 2
print(max_dist)