class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]
 
class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
 
class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
from test import *
a=str(input("Задайте вопрос"))
i=0
n=5
lesson = Data('Тогда надо лечить ', 'Django', 'Java', 'JavaScript', 'PHP',"Vue")
marIvanna = Teacher()
grusha = Pupil()
apple = Pupil()
grusha.knowledge
apple.knowledge
for i in range(0,n):
    if i==1:
        marIvanna.teach(lesson[1], grusha)        
        print("Болезнь груши ",grusha.knowledge)        
    elif i==2:
        marIvanna.teach(lesson[2], apple)
        print("Болезнь груши ",grusha.knowledge)     
    elif i==3:
        marIvanna.teach(lesson[3], grusha)
        print("Болезнь груши ",grusha.knowledge)   
    elif i==4:
        marIvanna.teach(lesson[4], apple)
    elif i==5:
        marIvanna.teach(lesson[5], grusha)
        print("Болезнь груши ",apple.knowledge)
    else:
        print("У вас больше нет воросов")
    

       