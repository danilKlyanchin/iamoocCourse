from myinterval import Interval as Interval_my
from mybox import Box
from myring import contract_s
from myestimator import sivia
from vibes import vibes
from pyibex.pyibex import CtcFwdBwd, Function, Interval, IntervalVector
from myseparator import draw_box_contour


def f(x: Box) -> Box:
    return Box((x[0] - c[0]).sqr() + (x[1] - c[1]).sqr())


if __name__ == "__main__":
    c = Box(Interval_my(1, 3), Interval_my(2, 4))
    r = Interval_my(2, 4)
    x, y = Interval_my(-10, 10), Interval_my(-10, 10)

    vibes.beginDrawing()
    vibes.newFigure('Set S')
    vibes.setFigureSize(1000, 500)
    sivia(f, Box(r.sqr()), Box(x, y), eps=0.1)

    # Define a Function from an equation
    func = Function("x", "y", "(x-1)^2 + (y - 2)^2")
    # FwdBwd Contractor
    ctc1 = CtcFwdBwd(func, Interval(-10, 10))
    tmp = IntervalVector(2, Interval(-10, 10))
    ctc1.contract(tmp)

    print('initial box', x, y)
    print('contract s', ax, ab)
    print('ctc1', tmp)  

    vibes.endDrawing()
