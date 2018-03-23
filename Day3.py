input = 325489
y = 1
x = 1
full = 0
remainder = 0
z = 1
while True:
    y += 2
    x = y ** 2
    z = y
    if x > input:
        full = z**2
        print(z)
        remainder = z**2 - input
        print(remainder)
        break

rem2 = remainder % z
print("Remainder2")
print(rem2)
distance = abs(int(z/2) - rem2)
print("Distance")
print(distance)
print("From border to the center(to 1)")
print(int((z-1)/2))
result = distance + int((z-1)/2)
print(result)

# Part two

# https://oeis.org/A141481
