from numpy import linspace
import matplotlib.pyplot as plt
from trapezoidal import trapezoidal

def main():
	# Сравнение с точным решением
w = lambda x:exp(x**3)
exact = w(1) - w(0)
print("Значение exact равно",exact)
error = exact - numerical #abs((exact - numerical)/exact*100)
print("Значение error равно",error )
 

def application():
	from math import exp
	v = lambda x: 3*x**2*exp(x**3)
	n = input('n: ')
	numerical = trapezoidal(v, 0, 1, n)
V = lambda x: exp(x**3)
exact = V(1) - V(0)
	