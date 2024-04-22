from sympy import limit, Symbol, sin, oo
from sympy import diff, Symbol, sin, tan
x = Symbol("x")
print("Предел sin(x)/x приx-->0 равно",limit(sin(x)/x, x, 0))
print("Предел sin(x)/x приx-->oo равно",limit(sin(x)/x, x, oo))

print(diff(sin(x), x)) #cos(x)
print(diff(sin(2*x), x))#2*cos(2*x)
print (diff(tan(x), x))  #tan (x)**2 + 1

# Разложение в ряд с использованием метода .series(var, point, order):
from sympy import Symbol, cos
x = Symbol('x')
print("Разложение в ряд с использованием метода .series(var, point, order):",cos(x).series(x, 0, 10))
from sympy import Integral, pprint

y = Symbol("y")
e = 1/(x + y)
s = e.series(x, 0, 5)

