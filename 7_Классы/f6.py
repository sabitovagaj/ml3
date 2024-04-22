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
lesson = Data('Python', 'Django', 'Java', 'JavaScript', 'PHP',"Vue")
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
a=5
if a==5:
    marIvanna.teach(lesson[3], vasy)
else:
    marIvanna.teach(lesson[2], pety)
vasy.knowledge
pety.knowledge
print("Вася хорошо владеет с языками ",vasy.knowledge)
print("А Петя хорошо владеет с языками ",pety.knowledge)

       