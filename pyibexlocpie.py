from vibes import vibes
from pyibex.pyibex import *
from pyibex.geometry import SepPolarXY

M = [[6, 12], [-2, -5], [-3, 10], [3, 4]]
D = [Interval(10, 13), Interval(8, 10), Interval(5, 7), Interval(6, 8)]
A = [Interval(0.5, 1), Interval(-3, -3/2), Interval(1, 2), Interval(2, 3)]

vibes.beginDrawing()
vibes.newFigure(f'P1')
vibes.setFigureSize(1000, 500)

P0 = IntervalVector(2, Interval(-13, 13))

seps = []

for m, d, a in zip(M, D, A):
    pass


vibes.endDrawing()