from mybox import *
from myinterval import *
import numpy as np
from vibes import vibes


def f(x: Box) -> Box:
    tmp = Box()
    t = [0.2, 1, 2, 4]
    for i in range(4):
        # pass
        tmp.add(x[0] * (x[1] * (t[i])).exp())
    return tmp


def sivia(f, Y, initBox, eps=0.1, q=1):
    if isinstance(Y, Interval):
        Y = Box(Y)

    boxes = [initBox]
    while boxes:
        box = boxes.pop(0)
        if Y.contains(f(box), min_contains_count=q):
            vibes.drawBox(box[0].lb(), box[0].ub(), box[1].lb(), box[1].ub(), color='[red]')
        elif not Y.is_intersected(f(box), min_count=q):
            vibes.drawBox(box[0].lb(), box[0].ub(), box[1].lb(), box[1].ub(), color='[blue]')
            continue
        elif box.width() < eps:
            vibes.drawBox(box[0].lb(), box[0].ub(), box[1].lb(), box[1].ub(), color='[yellow]')
        else:
            box_left, box_right = box.split()
            boxes.append(box_left)
            boxes.append(box_right)


if __name__ == '__main__':
    y1 = Interval(1.5, 2)
    y2 = Interval(0.7, 0.8)
    y3 = Interval(0.1, 0.3)
    y4 = Interval(-0.1, 0.03)
    Y = Box(y1, y2, y3, y4)
    initBox = Box(Interval(-3, 3), Interval(-3, 3))

    vibes.beginDrawing()
    vibes.newFigure('estimator')
    vibes.setFigureSize(1000, 500)
    sivia(f, Y, initBox, 0.01, 1)
    vibes.endDrawing()
