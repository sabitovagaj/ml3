from math import sin,cos
def my_min(spisok):
    """Выводит мин значение"""
    vmin = spisok[0] # необходимо для начального значения мин списка
    for i in spisok:
        if i < vmin:
            vmin = i
        return vmin
q = input("Введите число: ")
print("Ваша число", q)
q=int(q)
h=0.1
n=10
a=-1
b=-1
if q>=0:
    for i in range(-n, n):
        xi=a+i*h
        print("q=",q,"Зачение хi=",xi,"i=",i)
        sum=0
        for j in range(-n, n):
            yj=-b+j*h
        sum=sum+xi*q*cos(yj)
        f=sum
        if i<0:
            bi=f
        elif i==0:
            bi=f+1
        else:
            bi=f-1
        l=[bi]
        print("Зачение при xi=",xi,"f=",f,"Значение вектора L[",i,"]=",l,end="\t")
        print("\n")
else:
    for i in range(-n, n):
        xi=a+i*h
        print("q=",q,"Зачение хi=",xi,"i=",i)
        p=1
        for j in range(-n, n):
            yj=-b+j*h
        p=p*xi*q*cos(yj)
        f=p
        if i<0:
            bi=f
        elif i==0:
            bi=f+1
        else:
            bi=f-1
        l=[-bi]
        print("Зачение при xi=",xi,"fp=",f,"Значение вектора L[",i,"]=",l,end="\t")
        print("\n")
print ("Минимальное значение вектора L равно",my_min(l))




        
      