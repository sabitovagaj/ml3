from math import sin,cos
b = input("Введите число: ")
print("Ваша число равно,", b)
b=int(b)
h=0.1
n=2
a=-1
i=0
if b>=0:
    for i in range(0, 10):
        xi=a+i*h
        print("b=",b,"Зачение хi=",xi,"i=",i)
        sum=0
        for j in range(0, 10):
            yj=a+j*h
        sum=sum+xi*b*cos(yj)
        f=sum
        print("Зачение при xi=",xi,"f=",f,end="\t")
        print("\n")
else:
    for i in range(0, 10):
        xi=a+i*h
        print("b=",b,"Зачение хi=",xi,"i=",i)
        p=1
        for j in range(1, 10):
            yj=a+j*h
        p=p*xi*b*cos(yj)
        f=p
        print("Зачение при xi=",xi,"p=",p,end="\t")
        print("\n")
            

          
            

           

   

 