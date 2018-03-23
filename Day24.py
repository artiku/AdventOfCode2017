import re
import collections

# with open("day24input.txt") as f:
#     content = f.readlines()
#
# content = [x.strip() for x in content]


with open("day24input.txt") as f:
    input = f.readlines()
    input = " ".join(input)

def gen_bridges(bridge, components):
    bridge = bridge or [(0, 0)]
    cur = bridge[-1][1]
    for b in components[cur]:
        if not ((cur, b) in bridge or (b, cur) in bridge):
            new = bridge+[(cur, b)]
            yield new
            yield from gen_bridges(new, components)


def parse_components(input):
    components = collections.defaultdict(set)
    for l in input.strip().splitlines():
        a, b = [int(x) for x in l.split('/')]
        components[a].add(b)
        components[b].add(a)
    return components


def solve(input):
    components = parse_components(input)
    mx = []
    for bridge in gen_bridges(None, components):
        mx.append((len(bridge), sum(a+b for a, b in bridge)))
    return mx


solution = solve(input)
part1 = sorted(solution, key=lambda x: x[1])[-1][1]
print(part1)
part2 = sorted(solution)[-1][1]
print(part2)

# bridge_list = []
#
# def req(not_used_elems, current_pin, bridge):
#     for elem in not_used_elems:
#         pin1, pin2 = elem.split("/")
#         if pin1 == current_pin:
#             not_used_elems_copy = not_used_elems.copy()
#             not_used_elems_copy.remove(elem)
#             req(not_used_elems_copy, pin2, bridge + " " + elem)
#         elif pin2 == current_pin:
#             not_used_elems_copy = not_used_elems.copy()
#             not_used_elems_copy.remove(elem)
#             req(not_used_elems_copy, pin1, bridge + " " + elem)
#     bridge_list.append(bridge)
#     return bridge
#
#
# for bridge_elem in content:
#     pin1, pin2 = bridge_elem.split("/")
#     if pin1 == "0":
#         content.remove(bridge_elem)
#         req(content[:], pin2, bridge_elem)
#     if pin2 == "0":
#         content.remove(bridge_elem)
#         req(content[:], pin1, bridge_elem)
#
# maxi = 0
# for elem in bridge_list:
#     nums = re.findall(r"[\d']+", elem)
#     sum = 0
#     for num in nums:
#         sum += int(num)
#     if sum > maxi:
#         maxi = sum
# print(maxi)
