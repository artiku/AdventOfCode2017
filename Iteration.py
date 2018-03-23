import math


def boo(x):
    return (20 * x * math.cos(x) + 3 + 20 * math.sin(x)) / (20 * math.cos(x) - 10)


def f(x):
    return x - foo(x)/fderivative(x)


def fderivative(x):
    return 1/2 - math.cos(x)


def foo(x):
    return x/2 - 3/20 - math.sin(x)


i = 1
x0 = 2
x1 = x0
eps = 0.00001

while True:
    #print(str(i) + ". x = " + str(x1) + "\t abs = " + str(abs(x1 - x0)))
    x0 = x1
    x1 = f(x0)

    print(str(i) + ". x = " + str(x1) + "\t abs = " + str(abs(x1 - x0)))
    i += 1
    if abs(x1 - x0) < eps: break
