import random
from math import sqrt

from .module3 import constant2, constant1


class TestA:
    def __init__(self):
        self.i = random.randint(1, 1)

    def compute(self):
        return self.i * 64


def super_sqrt(n):
    return constant2() * sqrt(n) + constant1()
