from vibes import vibes
from pyibex.pyibex import *
import pyibex

T = [0.2, 1, 2, 4]
Y = [
    Interval(1.5, 2),
    Interval(0.7, 0.8),
    Interval(0.1, 0.3),
    Interval(-0.1, 0.03)
]

seps = []
for t, y in zip(T, Y):
    f = Function('p1', 'p2', f'p1 * exp(p2 * {t})')
    sep = SepFwdBwd(f=f, itv_y=y)
    seps.append(sep)

P = IntervalVector(2, Interval(-3, 3))

# question 1
# for i in range(4):
#     vibes.beginDrawing()
#     vibes.newFigure(f'P_{i}')
#     vibes.setFigureSize(1000, 500)
#     vibes.axisLimits(-4, 4, -4, 4)
#     pyibex.pySIVIA(P, seps[i], epsilon=0.01)

# question 2
S = SepQInterProjF(seps)
for q in range(3):
    S.q = q
    vibes.beginDrawing()
    vibes.newFigure(f'P^{q}')
    vibes.setFigureSize(1000, 500)
    vibes.axisLimits(-4, 4, -4, 4)
    pyibex.pySIVIA(P, S, epsilon=0.01)

print('Results are the same as it was obtained in ex 4!')
