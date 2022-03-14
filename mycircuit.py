from myinterval import *
from mybox import Box


def contractor_sum(x, y, z) -> [Interval, Interval, Interval]:
    x_ = x.copy()
    y_ = y.copy()
    z_ = z.copy()
    # z = x + y
    z_ = z_.intersect(x_ + y_)
    # x = z - y
    x_ = x_.intersect(z_ - y_)
    # y = z - x
    y_ = y_.intersect(z_ - x_)
    return x_, y_, z_


def contractor_mul(x, y, z):
    x_ = x.copy()
    y_ = y.copy()
    z_ = z.copy()
    # z = x * y
    z_ = z_.intersect(x_ * y_)
    # x = z / y
    x_ = x_.intersect(z_ / y_)
    # y = z / x
    y_ = y_.intersect(z_ / x_)
    return x_, y_, z_


def contractor_sqr(x: Interval, y: Interval) -> [Interval, Interval]:
    y_ = y.intersect(x.sqr())

    if y.lb() <= 0:
        return x.intersect(Interval(-y_.sqrt().ub(), y_.sqrt().ub())), y_

    x_ = Box()
    if not x.intersect(y_.sqrt()).is_empty:
        x_.add(x.intersect(y_.sqrt()))
    if not x.intersect(y_.sqrt() * (-1)).is_empty:
        x_.add(x.intersect(y_.sqrt() * (-1)))

    if x_.size() == 1:
        return x_[0], y_
    return x_[0].union(x_[1]), y_


def calculate_R1_R2(P, I, U1, U2, E):
    R1 = Interval(0, float('inf'))
    R2 = Interval(0, float('inf'))
    R = Interval(0, float('inf'))
    U = U1 + U2 - R
    I, U, P = contractor_mul(I, U, P)
    I, R1, U1 = contractor_mul(I, R1, U1)
    I, R2, U2 = contractor_mul(I, R2, U2)
    _, R, P = contractor_mul(I.sqr(), R, P)
    R1, R2, R = contractor_mul(R1, R2, R)
    return R1, R2


if __name__ == '__main__':
    # Equestions that were used
    # P = I * U, U = U1 + U2 - E
    # U1 = I * R1
    # U2 = I * R2
    # P = I^2 * R
    # R = R1 + R2

    P = Interval(124, 130)
    I = Interval(4, 8)
    U1 = Interval(10, 11)
    U2 = Interval(14, 17)
    E = Interval(23, 26)

    R1, R2 = calculate_R1_R2(P, I, U1, U2, E)
    print(f'R1 = {R1}')
    print(f'R2 = {R2}')
