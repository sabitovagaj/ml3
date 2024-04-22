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
from test import *
lesson = Data('Надо лечить кабофосом', 'Избавиться от личинок бабочки', 'Лучше подкормит селитрой', 'Дать полив ', 'Не подлежит лечению')
Vrach = Lechenie()
kartoshka = Pupil()
pshenisa = Pupil()
apple = Pupil()
yachmen = Pupil()
oves = Pupil()
grusha = Pupil()
svekla=Pupil()
Vrach.teach(lesson[0], kartoshka, pshenisa)
Vrach.teach(lesson[1], pshenisa,apple,oves,grusha)
Vrach.teach(lesson[0], apple,pshenisa,kartoshka)
Vrach.teach(lesson[2], kartoshka, pshenisa)
Vrach.teach(lesson[3], pshenisa,apple)
Vrach.teach(lesson[0], apple,pshenisa,kartoshka)
kartoshka.knowledge
svekla.knowledge
pshenisa.knowledge
apple.knowledge
oves.knowledge
grusha.knowledge
yachmen.knowledge
print("Лечение картошки",kartoshka.knowledge)
print("Лечение пшеницы",pshenisa.knowledge,yachmen.knowledge)
print("Лечение яблоки",apple.knowledge,grusha.knowledge)
print("Лечение овесь",kartoshka.knowledge,svekla.knowledge)
print("Лечение груши",pshenisa.knowledge)
print("Лечение ячмень",apple.knowledge,grusha.knowledge)

       