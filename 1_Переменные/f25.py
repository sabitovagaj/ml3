from math import sin, pi,cos,tan

# Жалпы функциялар
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
# Трапеция аыкмасы
def summa_trap (a,b,number):
    s=0
    i=1;number1=number-1
    while i<=number1:
        y=a+i*((b-a)/number)
        s+=f(y)*g(y)
        i+=1 
        print("Значение суммы в  trap равно =",s)       
        return s
# Симпсон  ыкмасы
def summa_sympson (a,b,number):
    s1=0
    s2=0
    number=2*number
    for i in range(1,number):
        if i==2*number-1:
            y=a+i*((b-a)/number)
            s1+=f(y)*g(y)
        elif i==2*number-2:
            y=a+i*((b-a)/number)
            s2+=f(y)*g(y)
    s=2*s1+4*s2        
    print("Значение суммы в Симпсон равно",s)       
    return s        
n=100
a=-pi*0.5
b=pi*0.5
h=(b-a)/n
h1=(b-a)/(2*n)
vintegral_trap=h*(((f(a)*g(a)+f(b)*g(b))/2)+summa_trap(a,b,n))
vintegral_sympson=h1*(f(a)*g(a)+f(b)*g(b)+summa_sympson(a,b,n))/3
print("Значение интеграла  по методу трапеций равно",vintegral_trap)
print("Значение интеграла по методу Симпсона  равно",vintegral_sympson)
R=abs(vintegral_sympson-vintegral_trap)
print("Значение ошибки  равно",R)




