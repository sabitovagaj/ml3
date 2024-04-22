
def rectangular_double1(f, a, b, c, d, nx, ny):
	"""
	Вычисляет значение двойного интеграла по формуле прямоугольников
	при реализации двойной суммы
	f - подынтегральная функция
	a, b, c, d - границы прямоугольной области интегрирования
	nx, ny - количество частичных отрезков по x и y соответственно
	"""
	hx = (b - a)/float(nx)
	hy = (d - c)/float(ny)
	I = 0
	for i in range(nx):
		for j in range(ny):
			xi = a + hx/2 + i*hx
			yj = c + hy/2 + j*hy
			I += hx*hy*f(xi,yj)
	return I
f = lambda x, y: 2*x + y
rectangular_double1(f, 0, 2, 2, 3, 5, 5)
print(rectangular_double1(f, 0, 2, 2, 3, 5, 5))