from math import sqrt
a=input("Введите число а")
a=int(a)
print("Число а равно",a)
b=input("Введите число b")
print("Число а равно",b)
c=input("Введите число c")
print("Число а равно",c)
# a=float(a)
b=float(b)
c=float(c)
d=float(b*b-4*a*c)
print("Дискриминант равно",d)
if d>0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print("x1=",x1,"x2=",x2)
elif d==0:
    x1=-b/(2*a)
    x2=x1
    print("x1=",x1,"x2=",x2)
else:
    print("Данное уравнение имеет комплексные корни")
    
    
