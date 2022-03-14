from myinterval import *
from mybox import *
from mycircuit import contractor_sqr


def contract_s(x, y, cx, cy, r):
    x_ = x.copy()
    y_ = y.copy()
    # forward
    a = x_ - cx
    b = a.sqr()
    c = y_ - cy
    d = c.sqr()
    e = b + d
    e = r.sqr()
    # backward

    b = b.intersect(e - d)
    d = d.intersect(e - b)
    if d.is_empty and b.is_empty:
        return b, d
    c, _ = contractor_sqr(c, d)
    y_ = y_.intersect(c + cy)
    a, _ = contractor_sqr(a, b)
    x_ = x_.intersect(a + cx)
    return x_, y_


if __name__ == '__main__':
    c = Box(Interval(1, 1), Interval(2, 2))
    r = Interval(3, 3)
    x = Interval(-float('inf'), float('inf'))
    y = Interval(-float('inf'), float('inf'))

    print('Outer approximation for S')
    print(contract_s(x, y, c[0], c[1], r))
