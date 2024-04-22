class Student :
    def f (self, n, y):
        self.name=n
        self.year=y
        print (self.name, "учиться на  ", self.year, "курсе")
s1=Student()
s2=Student()
s1.f ("Асанов А.", 5)
s2.f ("Усенов У.", 6)
