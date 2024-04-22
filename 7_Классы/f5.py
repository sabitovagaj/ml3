class Person:
	name = "Ivan"
	age = 10
	
	def __set(self, name, age):
		self.name = name
		self.age = age
		
class Student (Person):
	course = 1

igor = Student ()
igor._Person__set ("Igor", 19)
igor.course = 2
print (igor.course)

vlad = Person ()
vlad._Person__set ("Влад", 25)
print (vlad.name + " " + str(vlad.age))

ivan = Person ()
ivan._Person__set ("Иван", 56)
print (ivan.age)