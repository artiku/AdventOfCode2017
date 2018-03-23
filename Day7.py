# Pt1
content = []
# with open("day7input.txt") as f:
#     for line in f.readlines():
#         content.extend(line.replace(",", "").split())
# for x in content:
#     if content.count(x) == 1:
#         print(x)

with open("day7input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

programs = {}
program_dependency_dict = {}
program_layer_dict = {}
program_total_weight_dict = {}


def calc_total_weight(program):
    if program in program_dependency_dict:
        sum = 0
        sum += programs[program]
        for inner_node in program_dependency_dict[program]:
            sum += calc_total_weight(inner_node)
        return sum
    else:
        return programs[program]


def check_dependencies(node):
    if node in program_dependency_dict:
        for inner_node in program_dependency_dict[node]:
            program_layer_dict[inner_node] = program_layer_dict.get(inner_node, 0) + 1
            check_dependencies(inner_node)


for row in content:
    row = row.split("->")
    if len(row) == 2:
        program, weight = row[0].split()
        programs[program] = int(weight.replace("(", "").replace(")", ""))
        dependency_list = row[1].strip().split(", ")
        program_dependency_dict[program] = dependency_list
    else:
        program, weight = row[0].split()
        programs[program] = int(weight.replace("(", "").replace(")", ""))

for dependency_list in program_dependency_dict.values():
    for node in dependency_list:
        program_layer_dict[node] = program_layer_dict.get(node, 0) + 1
        check_dependencies(node)
        program_total_weight_dict[node] = calc_total_weight(node)

for dependency_list in program_dependency_dict.values():
    last = 0
    for node in dependency_list:
        if program_layer_dict[node] == 3:
            # if node == "gozhrsf":
            #     print(program_total_weight_dict[node])
            #     print(program_total_weight_dict["ifxzdfy"])
            #     print(program_total_weight_dict["zyqssjb"])
            #     print(program_total_weight_dict["uuxpvxf"])
            #     print(program_total_weight_dict["hpziqqg"])
            #     print(program_total_weight_dict["abxglwt"])
            #     print(program_total_weight_dict["oqjqu"])
            #     print(program_total_weight_dict["vhkodl"])
            current = program_total_weight_dict[node]
            # print(current)
            # print(node)
            if last != 0 and current != last:
                print("Here!")
                print(programs[node] + (last - current))
                print(node)
            else:
                last = current
