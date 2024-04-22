# Метод  __init__()
# Если для класса определен метод __init__(), то он авто­ 
# матически вызывается  сразу после создания экземпляра
# класса.
class Student:
    def __init__(self, c,d):
        self.vuz=c
        self.spesialnost=d
    def f (self,n,m,y):
        self.name=n
        self.kurs=m        
        self.year=y
        print( "ФИО:",self.name,"курс",self.kurs,self.year, "лет")
s=Student("ВУЗ:КГУ им.И.Арабаева","Специальность:Прикладная информатика ")
print(s.vuz)
print(s.spesialnost)
s.f("Асанов А.А.",3,20)
s.f("Усенов У.У.",4,21)
s.name
print(s.name)


                    
       
