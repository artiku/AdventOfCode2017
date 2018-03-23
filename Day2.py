with open("day2input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
sum = 0
for row in content:
    split_rows = row.split()
    row_max = int(split_rows[0])
    row_min = int(split_rows[0])
    for num in split_rows:
        if int(num) > row_max:
            row_max = int(num)
        elif int(num) < row_min:
            row_min = int(num)
    sum += row_max - row_min

# Part two

sum = 0
for row in content:
    split_rows = row.split()
    for num in split_rows:
        for num1 in split_rows:
            if int(num1) % int(num) == 0 and num1 != num:
                sum += int(num1) / int(num)
                break
print(sum)