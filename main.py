from vibes import vibes
from myinterval import *
from myminimizer import *
import numpy as np

# Exercise 3
def f(x):
  if isinstance(x, Interval):
    return x.sqr() + x * 2 - x.exp()
  return x**2 + 2*x - np.exp(x)


minimizer = minimize_function(f, Interval(-2, 2), plot_flag=True)
print(f'minimizer is {minimizer}')
print(f'Interval containing the global minimum is {f(minimizer)}')

