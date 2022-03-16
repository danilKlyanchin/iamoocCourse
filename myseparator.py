from myinterval import Interval
from mybox import Box
from myring import contract_s
from mycircuit import contractor_sqr
from myestimator import sivia
from vibes import vibes


def contract_s_outer(x, y, cx, cy, r):
    def out_of(first, second):
        if second.contains(first):
            return Box()
        if first.contains(second) and first.lb() != second.lb() and first.ub() != second.ub():
            return Box().add(Interval(first.lb(), second.lb())).add(Interval(second.ub(), first.ub()))
        if first.lb() < second.lb() < first.ub():
            return Box().add(Interval(first.lb(), second.lb()))
        if first.lb() < second.ub() < first.ub():
            return Box().add(Interval(second.ub(), first.ub()))
        return Box().add(first.copy())

    def backward(a, b, c, d, cx, cy, interval):
        b = b.intersect(interval - d)
        d = d.intersect(interval - b)
        c, _ = contractor_sqr(c, d)
        a, _ = contractor_sqr(a, b)
        y_ = y.intersect(c + cy)
        x_ = x.intersect(a + cx)
        return x_, y_

    a = x - cx
    b = a.sqr()
    c = y - cy
    d = c.sqr()
    e = b + d

    e = out_of(e, r.sqr())
    if e.size() == 0:
        print('here1')
        return Interval(0, 0, True), Interval(0, 0, True)

    x_ans, y_ans = Interval(0, 0, True), Interval(0, 0, True)
    for i in range(e.size()):
        x_, y_ = backward(a, b, c, d, cx, cy, e[i])
        x_ans = x_ans.union(x_)
        y_ans = y_ans.union(y_)

    return x_ans, y_ans


def separator_s(x, y, c, r):
    a1, a2 = contract_s(x, y, c[0], c[1], r)
    a = Box(a1, a2)
    b1, b2 = contract_s_outer(x, y, c[0], c[1], r)
    b = Box(b1, b2)
    return a, b


def separator_s_union(x, y, c1, c2, r1, r2):
    a1, b1 = separator_s(x, y, c1, r1)
    a2, b2 = separator_s(x, y, c2, r2)
    return a1.union(a2), b1.union(b2)


def separator_s_intersection(x, y, c1, c2, r1, r2):
    a1, b1 = separator_s(x, y, c1, r1)
    a2, b2 = separator_s(x, y, c2, r2)
    return a1.intersect(a2), b1.intersect(b2)


def f1(x: Box) -> Box:
    return (x[0] - c1[0]).sqr() + (x[1] - c1[1]).sqr()


def f2(x: Box) -> Box:
    return (x[0] - c2[0]).sqr() + (x[1] - c2[1]).sqr()


def f12(x):
    return Box(f1(x), f2(x))


def draw_box_contour(x_ax, y_ax, color):
    vibes.drawLine([[x_ax.lb(), y_ax.lb()], [x_ax.lb(), y_ax.ub()]], color=f'{color}')
    vibes.drawLine([[x_ax.lb(), y_ax.ub()], [x_ax.ub(), y_ax.ub()]], color=f'{color}')
    vibes.drawLine([[x_ax.ub(), y_ax.ub()], [x_ax.ub(), y_ax.lb()]], color=f'{color}')
    vibes.drawLine([[x_ax.ub(), y_ax.lb()], [x_ax.lb(), y_ax.lb()]], color=f'{color}')


if __name__ == '__main__':
    c1 = Box(Interval(1, 1), Interval(2, 2))
    r1 = Interval(4, 5)
    c2 = Box(Interval(2, 2), Interval(5, 5))
    r2 = Interval(5, 6)

    x = Interval(-14, 14)
    y = Interval(-14, 14)

    a1, b1 = separator_s(x, y, c1, r1)
    a2, b2 = separator_s(x, y, c2, r2)

    # question 1
    # Separator S
    # print('An example of separator for S1')
    # print('in', a1)
    # print('out', b1)

    # question 2
    # Intersection
    # vibes.beginDrawing()
    # vibes.newFigure('Intersection S1 and S2')
    # vibes.setFigureSize(1000, 500)
    # sivia(f=f12, Y=Box(r1.sqr(), r2.sqr()), initBox=Box(x, y), eps=0.01, q=2)
    # # Separator for intersection of S1 and S2
    # inter_box_S_inner, inter_box_S_outer = separator_s_intersection(x, y, c1, c2, r1, r2)
    # print('Separator of intersection S1 and S2')
    # print('in', inter_box_S_inner)
    # print('out', inter_box_S_outer)
    # vibes.endDrawing()

    # question 3
    # Union
    vibes.beginDrawing()
    vibes.newFigure('Union S1 and S2')
    vibes.setFigureSize(1000, 500)
    sivia(f=f12, Y=Box(r1.sqr(), r2.sqr()), initBox=Box(Interval(-20, 20), Interval(-20, 20)), eps=0.01, q=1)
    # Separator for union of S1 and S2
    union_box_S_inner, union_box_S_outer = separator_s_union(x, y, c1, c2, r1, r2)
    print('Separator of union S1 and S2')
    print('in', union_box_S_inner)
    print('out', union_box_S_outer)
    vibes.endDrawing()
