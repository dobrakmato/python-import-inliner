import random

from .module2 import TestA, super_sqrt
from .module3 import (
    constant1,
    constant2
)


class TestB:
    def __init__(self):
        self.c = random.randint(1, 1)

    def result(self):
        inst = TestA()
        a = inst.compute()
        b = super_sqrt(a)
        c = constant1()
        return a * b + c - constant2() + self.c
