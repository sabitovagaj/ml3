from math import sin,cos,pi

def my_min(spisok):
    """Выводит мин значение"""
    vmin = spisok[0] # необходимо для начального значения мин списка
    for i in spisok:
        if i < vmin:
            vmin = i
        return vmin
def my_max(spisok):
    """Выводит мин значение"""
    vmax = spisok[0] # необходимо для начального значения мин списка
    for i in spisok:
        if i > vmax:
            vmax = i
        return vmax        
n=10
for i in range(0, n):
        for j in range(0, n):
                d=sin(pi*0.765)*i+cos(pi*0.8765)*j
                print("i=",i,"j=",j,"Зачение d=",d)
                l=[d]
                print("i=",i,"Зачение l[",i,"]","[",j,"]=",l)
        print("Цикл при i=",i,"для обращению к функции my_min")        
        print("Минимальное число в списке равно",my_min(l))
        m=[l]
        print("Образуем новый список для обращения к my_max m[",i,"]=",m)
print("Находиv максимальное число в списке m =",my_max(m))            
                          
                                                                      
        