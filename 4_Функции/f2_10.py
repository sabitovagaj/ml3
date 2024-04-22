from numpy import linspace
from math import exp,sin,cos
import matplotlib.pyplot as plt

def trapezoidal(f, a, b, n):
	""" 
	Вычисляет приближенное значение интеграла с помощью формулы трапеций
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
	h = float(b - a)/n
	result = 0.5*(f(a) + f(b))
	for i in range(1, n):
		result += f(a + i*h)
	result *= h
	return result

V = lambda x: exp(x**3)+x**2-cos(x)
n=100
I = trapezoidal(V, 0, 1, n)
print("Значение интеграла равно",I)
exact = V(1) - V(0)
error=exact - I    
print("Значение ошибки равно",error)
