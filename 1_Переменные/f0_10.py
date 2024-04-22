from math import sin, pi,cos,tan
def f(x):
    if x>=0:
        result=x+1
    else:
        result=cos(x)
    return result
def g(t):
    if t<0:
        result=t+sin(t)
    elif t==0:
        result= tan(t)   
    else:
        result=pi/2   
    return result
def summa (a,b,number):
    s=0
    i=1;number1=number-1
    while i<=number1:
        y=a+i*((b-a)/number)
        s+=f(y)*g(y)
        i+=1 
        print("Значение суммы равно",s)       
        return s
n=100
a=-pi*0.5
b=pi*0.5
h=(b-a)/n
vintegral=h*(((f(a)*g(a)+f(b)*g(b))/2)+summa(a,b,n))
d=((f(a)*g(a)+f(b)*g(b))/2)
print("Значение d равно",d)
print("Значение интеграла равно",vintegral)



