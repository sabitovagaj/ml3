class Vehicle(object):
    """Некоторая строка документа"""
    
    def __init__(self, color, dvery, shina, tormoz):
        """Конструктор"""
        self.color = color
        self.dvery = dvery
        self.shina = shina
        self.tormoz = tormoz
    
    def tormozi(self):
        """
       Стоп машина
        """
        return "%s тормози" % self.tormoz
    
    def dvigaisy(self):
        """
        двигайся  авто
        """
        return "Я вожу %s %s!" % (self.color, self.tormoz)
 
 
if __name__ == "__main__":
    mersedes = Vehicle("Синий", 5, 4, "Мерседес")
    print(mersedes.tormozi())
    print(mersedes.dvigaisy())
 
    gruz_avto = Vehicle("красную", 3, 6, "грузовую  машину")
    print(gruz_avto.dvigaisy())
    print(gruz_avto.tormozi())
