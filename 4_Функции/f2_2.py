from math import cos,pi
def f(x):
     return 2*x
def q(x):
     return 2*x+3+cos(pi*0.456)    
y=f(2)*(1+f(6))*q(0.456)
print('Значение y равно ', y)