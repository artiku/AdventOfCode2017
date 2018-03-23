with open("day8input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

registers = {}
max_value = 0
for row in content:
    split_row = row.split()
    reg = split_row[0]
    action = split_row[1]
    amount = int(split_row[2])
    reg1 = split_row[4]
    evaluation = split_row[5]
    eval_value = int(split_row[6])
    if action == "inc":
        if evaluation == ">=" and registers.get(reg1, 0) >= eval_value:
            registers[reg] = registers.get(reg, 0) + amount
        elif evaluation == "<=" and registers.get(reg1, 0) <= eval_value:
            registers[reg] = registers.get(reg, 0) + amount
        elif evaluation == "==" and registers.get(reg1, 0) == eval_value:
            registers[reg] = registers.get(reg, 0) + amount
        elif evaluation == "!=" and registers.get(reg1, 0) != eval_value:
            registers[reg] = registers.get(reg, 0) + amount
        elif evaluation == "<" and registers.get(reg1, 0) < eval_value:
            registers[reg] = registers.get(reg, 0) + amount
        elif evaluation == ">" and registers.get(reg1, 0) > eval_value:
            registers[reg] = registers.get(reg, 0) + amount
    else:
        if evaluation == ">=" and registers.get(reg1, 0) >= eval_value:
            registers[reg] = registers.get(reg, 0) - amount
        elif evaluation == "<=" and registers.get(reg1, 0) <= eval_value:
            registers[reg] = registers.get(reg, 0) - amount
        elif evaluation == "==" and registers.get(reg1, 0) == eval_value:
            registers[reg] = registers.get(reg, 0) - amount
        elif evaluation == "!=" and registers.get(reg1, 0) != eval_value:
            registers[reg] = registers.get(reg, 0) - amount
        elif evaluation == "<" and registers.get(reg1, 0) < eval_value:
            registers[reg] = registers.get(reg, 0) - amount
        elif evaluation == ">" and registers.get(reg1, 0) > eval_value:
            registers[reg] = registers.get(reg, 0) - amount
    for key in registers.keys():
        if max_value < registers[key]:
            max_value = registers[key]


print("max", max_value)
max = 0
for key in registers.keys():
    if max < registers[key]:
        max = registers[key]
        max_key = key
print(max)
