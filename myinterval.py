import numpy as np


class Interval:
    def __init__(self, a: float, b: float, is_empty: bool = False):
        self.a = a
        self.b = b
        self.is_empty = is_empty

    def lb(self):
        return self.a

    def ub(self):
        return self.b

    def mid(self):
        return (self.a + self.b) / 2

    def diam(self):
        return self.b - self.a

    def __add__(self, other):
        if isinstance(other, Interval):
            return Interval(self.a + other.a, self.b + other.b)
        if isinstance(other, int) or isinstance(other, float):
            return Interval(self.a + other, self.b + other)
        raise AssertionError(f'Not implemented operation for class {type(other)}')

    def __sub__(self, other):
        if isinstance(other, Interval):
            elements = [self.a - other.a, self.a - other.b, self.b - other.a, self.b - other.b]
            return Interval(min(elements), max(elements))
        if isinstance(other, int) or isinstance(other, float):
            return Interval(self.a - other, self.b - other)
        raise AssertionError(f'Not implemented operation for class {type(other)}')

    def __mul__(self, other):
        if isinstance(other, Interval):
            if other.is_empty:
                return Interval(self.a, self.b, True)
            elements = [self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b]
            return Interval(min(elements), max(elements))
        if isinstance(other, int) or isinstance(other, float):
            if other > 0:
                return Interval(self.a * other, self.b * other)
            return Interval(self.b * other, self.a * other)
        raise AssertionError(f'Not implemented operation for class {type(other)}')

    def __truediv__(self, other):
        if isinstance(other, Interval):
            if other.is_empty:
                return Interval(self.a, self.b, True)
            sb = [self.a, self.b]
            ob = [other.a, other.b]
            if other.a * other.b < 0:
                ob.append(0)
            elements = [sb[i] / ob[j] if ob[j] != 0 else sb[i] * float('inf') for i in range(2) for j in range(2)]
            return Interval(min(elements), max(elements))
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                AssertionError(f'Division by zero in __truediv__ method of class Interval')
            return Interval(self.a / other, self.b / other)
        raise AssertionError(f'Not implemented operation for class {type(other)}')

    def exp(self):
        if self.is_empty:
            return Interval(0, 0, True)
        return Interval(np.exp(self.a), np.exp(self.b))

    def log(self):
        if self.is_empty or self.b < 0:
            return Interval(0, 0, True)
        if self.a * self.b < 0:
            return Interval(-float('inf'), np.log(self.b))
        return Interval(np.log(self.a), np.log(self.b))

    def sqr(self):
        if self.a * self.b < 0:
            return Interval(0, max(self.a ** 2, self.b ** 2))
        return Interval(min(self.a ** 2, self.b ** 2), max(self.a ** 2, self.b ** 2))

    def max(self, other):
        if self.is_empty * other.is_empty == 1:
            return Interval(max(self.a, other.a), max(self.b, other.b))
        if self.is_empty and other.is_empty:
            return Interval(0, 0, True)
        if self.is_empty:
            return Interval(other.a, other.b)
        return Interval(self.a, self.b)

    def sqrt(self):
        if self.is_empty or self.b < 0:
            return Interval(0, 0, 1)
        if self.a < 0:
            return Interval(0, np.sqrt(self.b))
        return Interval(np.sqrt(self.a), np.sqrt(self.b))

    def __repr__(self) -> str:
        if self.is_empty:
            return '[empty]'
        return f'[{self.a}, {self.b}]'

    def __str__(self) -> str:
        if self.is_empty:
            return '[empty]'
        return f'[{self.a}, {self.b}]'

    def contains(self, other) -> bool:
        if other.ub() <= self.ub() and other.lb() >= self.lb():
            return True
        return False

    def is_intersected(self, other):
        if other.lb() > self.ub() or other.ub() < self.lb():
            return False
        return True

    def copy(self):
        return Interval(self.a, self.b)

    def intersect(self, other):
        if not self.is_intersected(other):
            return Interval(0, 0, True)
        return Interval(max(self.a, other.lb()), min(self.b, other.ub()))

    def union(self, other):
        if self.is_empty:
            return other.copy()
        return Interval(min(self.lb(), other.lb()), max(self.ub(), other.ub()))
