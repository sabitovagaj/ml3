class Square: # Класстын аты чон тамгадан башталат
    width=0 # Озгорулмо
    height=0
    def area(self): #Метод
        return self.width*self.height
sq=Square() #Экземпляр класса
sq.width=100
sq.height=25
s_ar=sq.area()
print("Площадь прямоугольника равна s_ar=",s_ar)        