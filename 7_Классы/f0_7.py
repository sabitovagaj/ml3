class two_func:
    def __init__(self):#Считается как переменнная
        print("__init__ дает возможность переходит к выполнению  функций 1,2")
    def first_func(self):#Считается как атрибут-переменнная
        print(" Выполняется  первая функция")    
    def second_func(self):#Считается как атрибут-переменнная
        print("Выполняется  вторая функция")
def main():#Обьявляем новую общую функцию 
    rezyltat = two_func()#Создаем экземпляр класса
    rezyltat.first_func()#Обращаемся к первому атрибуту  обьекта
    # print(" Результат выпонения 1 функции",rezyltat.first_func())
    rezyltat.second_func()#Обращаемся к второму атрибуту  обьекта 
    # print("Результат выпонения 2 функции",rezyltat.second_func())
if __name__ == "__main__":
     main()