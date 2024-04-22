from math import exp
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
		result = result + f(a + i*h)
	result = result * h
	return result

V = lambda x: x**2
n=100
I = trapezoidal(V, 0, 1, n)
print("Интеграл=",I)
#Точное значение интеграла
tochnoe = V(1) - V(0)
eps=tochnoe-I
print("Ошибка равно ",eps)
