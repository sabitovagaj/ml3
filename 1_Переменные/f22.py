#Список , пример с применением обращения к *params через функции 
def f(*params):
    lo=[]
    lnol=[]
    lpol=[]
    for i in params:        
        if i<0:
           lo=lo+[i]            
           print("Отрицательные",lo)
           continue
        elif i==0:
            lnol=lnol+[i]
            print("Нулевые",lnol)
            continue
        else:
            lpol=lpol+[i]
            print("Положительные",lpol)
f(3,0,0,3,6,-6,9,-6,0,0,4,-67,-78,90,0,0,-43,-23,-12)




    







