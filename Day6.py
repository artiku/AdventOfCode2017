test_initial_list = [2, 4, 1, 2]
list_of_lists = []
list = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
count = 0

while list not in list_of_lists:
    list_of_lists.append(list[:])
    max_index = list.index(max(list))
    blocks = list[max_index]
    list[max_index] = 0
    while blocks > 0:
        max_index += 1
        if max_index >= len(list):
            max_index = 0
        list[max_index] += 1
        blocks -= 1
    count += 1
print(count)
# Part 2
print(count - list_of_lists.index(list))
