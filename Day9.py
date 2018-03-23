import re

with open("day9input.txt") as f:
    content = f.read()

print(content)
content = re.sub(r'!.?', '', content)
print(content)
part_two = re.findall(r'<.*?>', content)
sum_pt_two = 0
for garbage in part_two:
    sum_pt_two += len(garbage) - 2
print(sum_pt_two)
content = re.sub(r'<.*?>', '', content)
print(content)

opening_bracket = 0
sum = 0
for chara in content:
    if chara == "{":
        opening_bracket += 1
    if chara == "}":
        sum += opening_bracket
        opening_bracket -= 1
print(sum)

# m = re.search(r'{((,)?{}(,)?)+?}', content)
# print("groups")
# print(m.group(0))
# print(m.group(1))
# print(re.findall(r'{({})+?}', content))