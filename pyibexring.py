from vibes import vibes
from pyibex.pyibex import *
import pyibex


class myCtc(Ctc):
    def __init__(self):
        Ctc.__init__(self, 2)

    def contract(self, X):
        x, y = X[0], X[1]
        cx, cy, r = Interval(1, 3), Interval(2, 4), Interval(4, 5)
        a, b = x - cx, y - cy
        a2, b2, r2 = sqr(a), sqr(b), sqr(r)
        bwd_add(r2, a2, b2)
        bwd_sqr(a2, a)
        bwd_sqr(b2, b)
        bwd_sub(a, x, cx)
        bwd_sub(b, y, cy)


# question 1
vibes.beginDrawing()
vibes.newFigure('ring with pyibex')
vibes.setFigureSize(1000, 500)

X0 = IntervalVector(2, [-10, 10])
ctc = myCtc()
pyibex.pySIVIA(X0, ctc, 0.5)

# question 2
# vibes.beginDrawing()
# vibes.newFigure('ring with pyibex')
# vibes.setFigureSize(1000, 500)
#
# X0 = IntervalVector([[-10, 10], [-10, 10]])
# r = Interval(4, 5)
# f = Function("x1", "x2", "(x1-[1, 3])^2 + (x2-[2, 4])^2")
# ctc = CtcFwdBwd(f, sqr(r))
# pyibex.pySIVIA(X0, ctc, 0.5)


# # question 3
# vibes.beginDrawing()
# vibes.newFigure('ring with pyibex')
# vibes.setFigureSize(1000, 500)
# X0 = IntervalVector([[-10, 10], [-10, 10]])
#
# r1 = Interval(4, 5)
# f1 = Function("x[2]", "(x[0]-1)^2 + (x[1]-2)^2")
# sep1 = SepFwdBwd(f1, sqr(r1))
#
# r2 = Interval(5, 6)
# f2 = Function("x[2]", "(x[0]-2)^2 + (x[1]-5)^2")
# sep2 = SepFwdBwd(f2, sqr(r2))
#
# sep = sep1 & sep2
# pyibex.pySIVIA(X0, sep, 0.1)

# question 4
# vibes.beginDrawing()
# vibes.newFigure('ring with pyibex')
# vibes.setFigureSize(1000, 500)
# X0 = IntervalVector([[-10, 10], [-10, 10]])
#
# r1 = Interval(4, 5)
# f1 = Function("x[2]", "(x[0]-1)^2 + (x[1]-2)^2")
# sep1 = SepFwdBwd(f1, sqr(r1))
#
# r2 = Interval(5, 6)
# f2 = Function("x[2]", "(x[0]-2)^2 + (x[1]-5)^2")
# sep2 = SepFwdBwd(f2, sqr(r2))
#
# sep = sep1 | sep2
# pyibex.pySIVIA(X0, sep, 0.1)
