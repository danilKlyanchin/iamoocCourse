import numpy as np
from myinterval import *
from vibes import vibes


def minimize_function(f:callable, x:Interval, plot_flag : bool = False):
  
  def plot():
    x_points = np.linspace(x.lb(), x.ub(), 20)
    points = np.concatenate([x_points.reshape(-1, 1), f(x_points).reshape(-1, 1)], axis=1)
    vibes.beginDrawing()
    vibes.newFigure("Ex3")
    vibes.drawLine(points.tolist(), color="red[blue]")
    vibes.drawLine([[x.lb(), min_lb],[x.lb(), max_ub]], color="green")
    vibes.axisLimits(x.lb()-0.5, x.ub()+0.5, min_lb-1, max_ub+1)
    vibes.setFigureSize(500, 300)
    vibes.endDrawing()
  
  delta = [0.5, 0.05, 0.005, 0.0005]

  minimizer = Interval(0, 0, 1)
  for index in range(4):
    max_ub = 0
    min_lb = 0
    for k in range(int(4/delta[index])):
      x_k = Interval(k, k + 1) * delta[index] - 2
      f_interval = f(x_k)
      max_ub = max(max_ub, f_interval.ub())
      min_lb = min(min_lb, f_interval.lb())
      if minimizer.is_empty or f_interval.mid() < f(minimizer).mid():
        minimizer = x_k

  if plot_flag:
    plot();
  return minimizer