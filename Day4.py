import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)


with open("day4input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
valid = 0
for row in content:
    split_rows = row.split()
    if len(set(split_rows)) == len(split_rows):
        valid += 1
print(valid)

# Part 2
valid = len(content)
row_counter = 0
print(valid)
break_boo = False
for row in content:
    row_counter += 1
    split_rows = row.split()
    for word in split_rows:
        letter_list = list(word)
        if break_boo:
            break_boo = False
            break
        for word1 in split_rows:
            letter_list1 = list(word1)
            letter_list1.sort()
            letter_list.sort()
            if len(set(split_rows)) != len(split_rows):
                valid -= 1
                break_boo = True
                break
            if word1 != word and letter_list == letter_list1:
                print("Invalid Row number:", row_counter)
                print(letter_list1)
                print(letter_list)
                break_boo = True
                valid -= 1
                break
print(valid)
