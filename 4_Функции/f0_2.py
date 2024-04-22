from math import sin, pi,cos
def h(t):
    return (t**4 + 4*t)*cos(t)
def r(t):
    return sin(t**4 + 4*t) 

def f(t):
    return sin(t**4 + 4*t)+1
t=pi*0.00765 
q=r(pi*0.567)*f(4)   
g=h(0.1)*h(0.876)*sin(t)+q
print("g=",g,t,q)

# from math import sin, pi
# x = 2*pi
# dsin = diff(sin, x, h=1E-9)
# print("dsin=",dsin)