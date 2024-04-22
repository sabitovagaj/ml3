from  math import sin,cos

def f(x):
	f=(sin(x)+cos(x))**3
	return f
	
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
sumOfNumbers1 = trapezoidal(f, 2, 3, 100)      
print("Значение интеграла равно ",sumOfNumbers1)
 
