from math import asin, cos, radians, sin, sqrt
def func(x):
    f=sin(x)+asin(x)+sin(x+1)
    return f
def summa (a,b,number):
    s=0
    i=1;number1=number-1
    while i<=number1:
        y=a+i*((b-a)/number)
        s+=func(y)
        i+=1 
        print("Значение суммы равно",s)       
        return s  
number = int(input("Введите число: "))
a=0;b=1
h=(b-a)/number
integral=h*((func(a)+func(b))*0.5+summa(a,b,number))
print(" Значение интеграла равно",integral)

