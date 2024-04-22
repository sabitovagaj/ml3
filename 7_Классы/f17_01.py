class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]
 
class Lechenie:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
 
class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
class Data_rastenya:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]
 
class Lechenie_rasteniya:
    def teach_rasteniya(self, info, *pupil):
        for i in pupil:
            i.take(info)
 
class Pupil_rasteniya:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
class Pupil_korneplody:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)                
from test import *
lesson_rasteniya = Data_rastenya('Листья опрыскивать аммофосом', 'Избавиться от личинок бабочки', 'Лучше подкормит селитрой', 'Дать полив ', 'Не подлежит лечению')
Vrach_rasteniya = Lechenie_rasteniya()
lesson = Data('Хороший полив ', 'Подкормка селитрой', 'Лучше подкормит карбфосом ',"хороший результат дает аммофос", 'Дать полив ', 'Не подлежит лечению')
Vrach = Lechenie()
kartoshka = Pupil_korneplody()
pshenisa = Pupil_rasteniya()
apple = Pupil()
yachmen = Pupil_rasteniya()
oves = Pupil_rasteniya()
grusha = Pupil()
svekla=Pupil_korneplody()
Vrach.teach(lesson[0], kartoshka, pshenisa)
Vrach_rasteniya.teach_rasteniya(lesson[4], pshenisa,apple,oves,grusha)
Vrach.teach(lesson[3], apple,pshenisa,kartoshka)
Vrach.teach(lesson[2], kartoshka, svekla)
Vrach.teach(lesson[1], pshenisa,oves)
Vrach.teach(lesson[0], apple,grusha)
kartoshka.knowledge
svekla.knowledge
pshenisa.knowledge
apple.knowledge
oves.knowledge
grusha.knowledge
yachmen.knowledge
print("Общие рекомендации лечения: Корнеплодов : Растений : Фруктов и Овощей")
print("Лечение картошки",kartoshka.knowledge)
print("Лечение пшеницы",pshenisa.knowledge,yachmen.knowledge)
print("Лечение яблоки",apple.knowledge,grusha.knowledge)
print("Лечение овесь",kartoshka.knowledge,svekla.knowledge)
print("Лечение груши",pshenisa.knowledge)
print("Лечение ячмень",apple.knowledge,grusha.knowledge)