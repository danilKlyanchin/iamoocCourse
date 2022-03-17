from pyibex.pyibex import *
from vibes import vibes
import numpy as np


def rand(I):
    return np.random.uniform(I.lb(), I.ub(), size=1)[0]


def cstate(x1, y1, x, y, th):
    fx = Function('x1', 'x', 'th', f'x1 - x - 10 * {dt} * cos(th)')
    fy = Function('y1', 'y', 'th', f'y1 - y - 10 * {dt} * sin(th)')
    Cx = CtcFwdBwd(fx, Interval(0, 0))
    Cy = CtcFwdBwd(fy, Interval(0, 0))
    Bx = IntervalVector(3)
    Bx[0], Bx[1], Bx[2] = x1, x, th
    Cx.contract(Bx)
    x1, x, th = Bx[0], Bx[1], Bx[2]
    By = IntervalVector(3)
    By[0], By[1], By[2] = y1, y, th
    Cy.contract(By)
    y1, y, th = By[0], By[1], By[2]
    return x1, y1, x, y


def cmarks(x, y, mx, my, d):
    f = Function('x', 'y', 'mx', 'my', f'(x-mx)^2+(y-my)^2')
    C = CtcFwdBwd(f, sqr(d))
    X = IntervalVector(4)
    X[0], X[1], X[2], X[3] = x, y, mx, my
    C.contract(X)
    x, y, mx, my = X[0], X[1], X[2], X[3]
    return x, y, mx, my


vibes.beginDrawing()
vibes.newFigure('SLAM')
vibes.setFigureProperties({'x': 100, 'y': 100, 'width': 1400, 'height': 700})

_x, _y, _th, dt = 0, 0, 1, 0.1
_X, _Y = [], []
Th, J, D = [], [], []
_mx, _my = [6, -2, -3, 3], [1, -5, 4, 4]

noise = 0.03 * Interval(-1, 1)
kmax = 100

for k in range(kmax):
    j = np.random.randint(4)
    J.append(j)
    _d = np.sqrt((_mx[j] - _x) ** 2 + (_my[j] - _y) ** 2)
    D.append(_d + rand(noise) + noise)
    _X.append(_x)
    _Y.append(_y)
    Th.append(_th + rand(noise) + noise)
    _x += dt * 10 * np.cos(_th)
    _y += dt * 10 * np.sin(_th)
    _th += dt * (3 * np.sin(k * dt) ** 2 + rand(noise))

# Envelope the true trajectory
X = [Interval(-20, 20)] * (kmax + 1)
X[0] = Interval(0)
Y = X.copy()
Mx = [Interval(-20, 20)] * 4
My = [Interval(-20, 20)] * 4

for n in range(5):
    # contract trajectory
    for k in range(1, kmax):
        X[k], Y[k], X[k - 1], Y[k - 1] = cstate(X[k], Y[k], X[k - 1], Y[k - 1], Th[k - 1])

    for k in range(kmax, 1, -1):
        X[k], Y[k], X[k - 1], Y[k - 1] = cstate(X[k], Y[k], X[k - 1], Y[k - 1], Th[k - 1])

    # contract the positions of the landmarks
    for k in range(kmax):
        j = J[k]
        X[k], Y[k], Mx[j], My[j] = cmarks(X[k], Y[k], Mx[j], My[j], D[k])

    for Xk, Yk in zip(X, Y):
        vibes.drawBox(Xk.lb(), Xk.ub(), Yk.lb(), Yk.ub(), 'blue[cyan]')

    for j in range(4):
        vibes.drawBox(Mx[j].lb(), Mx[j].ub(), My[j].lb(), My[j].ub(), 'magenta[]')

# final approximations
for Xk, Yk in zip(X, Y):
    vibes.drawBox(Xk.lb(), Xk.ub(), Yk.lb(), Yk.ub(), 'blue[black]')

for j in range(4):
    vibes.drawBox(Mx[j].lb(), Mx[j].ub(), My[j].lb(), My[j].ub(), 'red[red]')

for j in range(4):
    vibes.drawCircle(_mx[j], _my[j], 0.06, 'red[blue]')

for k in range(kmax):
    vibes.drawCircle(_X[k], _Y[k], 0.03, 'black[magenta]')
