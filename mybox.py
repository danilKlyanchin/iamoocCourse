from myinterval import *


class Box:
    def __init__(self, *elements):
        self.intervals = []
        self.intervals.extend(elements)

    def add(self, x):
        self.intervals.append(x.copy())
        return self

    def size(self):
        return len(self.intervals)

    def __getitem__(self, key):
        if key >= len(self.intervals):
            raise AssertionError('Key is invalid')
        return self.intervals[key]

    def __setitem__(self, key, value):
        if key < 0 or key >= self.size():
            raise ValueError('Invalid key in setitem')
        self.intervals[key] = value

    def __repr__(self):
        box = ''
        for inter in self.intervals:
            box += str(inter) + ' '
        return box

    def boxes(self):
        return self.intervals

    def contains(self, other, min_contains_count=-1) -> bool:
        if self.size() != other.size():
            raise AssertionError('Sizes are different in contains')
        count = 0
        for i in range(self.size()):
            if self[i].contains(other[i]):
                count += 1
            if min_contains_count != -1 and count >= min_contains_count:
                return True
        return False

    def width_index(self):
        i_max = 0
        for i in range(self.size()):
            if self[i].diam() > self[i_max].diam():
                i_max = i
        return i_max

    def width(self):
        return self[self.width_index()].diam()

    def is_intersected(self, other, min_count=-1):
        if self.size() != other.size():
            raise AssertionError('Sizes are different in intersection')
        count = 0
        for i in range(self.size()):
            if self[i].is_intersected(other[i]):
                count += 1
        if min_count != -1 and count >= min_count:
            return True
        return False

    def copy(self):
        self_copy = Box()
        for i in range(self.size()):
            self_copy.add(self[i])
        return self_copy

    def split(self):
        box1 = self.copy()
        box2 = self.copy()
        index_max = self.width_index()
        box1[index_max] = Interval(box1[index_max].lb(), box1[index_max].mid())
        box2[index_max] = Interval(box2[index_max].mid(), box2[index_max].ub())
        return box1, box2

    def intersect(self, other):
        if self.size() != other.size():
            raise AssertionError('Sizes are different in intersection')
        ans = Box()
        for i in range(self.size()):
            ans.add(self[i].intersect(other[i]))
        return ans

    def union(self, other):
        if self.size() != other.size():
            raise AssertionError('Sizes are different in intersection')
        res = Box()
        for i in range(self.size()):
            res.add(self[i].union(other[i]))
        return res
