# ----- file __init__.py begin -----
# ----- file ./module1.py begin -----
import random

# ----- file ./module2.py begin -----
# import random
from math import sqrt

# ----- file ./module3.py begin -----
# ----- file ./subdir/module4.py begin -----
def delegated_constant2():
    return constant4() // 2


def constant4(): return 4
# ----- file ./subdir/module4.py end -----


def constant1():
    return 1


def constant2():
    return delegated_constant2()
# ----- file ./subdir/module4.py end -----


class TestA:
    def __init__(self):
        self.i = random.randint(1, 1)

    def compute(self):
        return self.i * 64


def super_sqrt(n):
    return constant2() * sqrt(n) + constant1()
# ----- file ./module3.py end -----
# from .module3 import (
#     constant1,
#     constant2
# )


class TestB:
    def __init__(self):
        self.c = random.randint(1, 1)

    def result(self):
        inst = TestA()
        a = inst.compute()
        b = super_sqrt(a)
        c = constant1()
        return a * b + c - constant2() + self.c
# ----- file ./module3.py end -----


def a():
    cls = TestB()
    print(cls.result())


a()
# ----- file ./module1.py end -----
