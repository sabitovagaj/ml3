
from numpy import np
def MonteCarlo_double(f, g, x0, x1, y0, y1, n):
	"""
	Численное интегрирование методом Монте-Карло функции
	f по области g >= 0, помещенной в прямоугольник
	[x0, x1]x[y0, y1].
	n^2 - количество случайных точек
	"""
	x = np.random.uniform(x0, x1, n)
	y = np.random.uniform(y0, y1, n)
	f_mean = 0          # среднее значение f
	num_inside = 0      # число точек, попавших в область интегрирования (g>=0)
	for i in range(len(x)):
		for j in range(len(y)):
			if(g(x[i], y[j]) >= 0):
				num_inside += 1
				f_mean += f(x[i], y[j])

	f_mean = f_mean/float(num_inside)
	area = num_inside/float(n**2)*(x1 - x0)*(y1 - y0)
	return area*f_mean
    
    g = lambda x, y: (1 if (0 <= x <= 2) and (3 <= y <= 4.5) else -1)
d=MonteCarlo_double(f, g, x0, x1, y0, y1, n)
print(d)
