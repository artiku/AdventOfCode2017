with open("day5input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
index = 0
step = 0
while 0 <= index < len(content):
    step += 1
    next_index = index + content[index]

    # Part 2
    if content[index] >= 3:
        content[index] -= 1
    else:
        content[index] += 1
    index = next_index
print(step)

