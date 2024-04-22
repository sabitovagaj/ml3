from math import sin,cos,pi

def f(*params):
    lo=[]
    lnol=[]
    lpol=[]
    for i in params:
        for j in params:
            aij=cos(i+1)*sin(j*pi+4.456)        
        if aij<0:            
           lo=lo+[aij]            
           print("Отрицательные aij=",lo)
           continue
        elif aij==0:
            lnol=lnol+[aij]
            print("Нулевые aij=",lnol)
            continue
        else:
            lpol=lpol+[aij]
            print("Положительные aij=",lpol)
f(13,0,0,23,16)