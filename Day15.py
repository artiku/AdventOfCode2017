from itertools import *


def genA(x=883):
    while True:
        x = x * 16807 % 2147483647
        yield x


def genB(x=879):
    while True:
        x = x * 48271 % 2147483647
        yield x

# or change func like this for pt2
#def genB(x=879):
#    while True:
#        x = x * 48271 % 2147483647
#        if x % 8 == 0:
#            yield x


# Part 1
#print(sum(starmap(
#    lambda a, b: a & 0xFFFF == b & 0xFFFF,
#    islice(zip_longest(genA(), genB()), 40000000))))

# Part 2

print(sum(starmap(
    lambda a, b: a & 0xFFFF == b & 0xFFFF,
    islice(zip_longest(filterfalse(lambda x: x % 4, genA()), filterfalse(lambda x: x % 8, genB())), 5000000))))
