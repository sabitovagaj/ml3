from trapezoidal import trapezoidal
from math import exp
  v = lambda x: 3*x**2*exp(x**3)
  n = 4
  I = trapezoidal(v, 0, 1, n)
  print("Интеграл равно",I)