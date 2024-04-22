class two_func:
    def first_func(self):#Считается как переменнная
        print("Результат выполнения первой функции")
    def second_func(self):#Считается как переменнная
        print("Результат выполнения второй функции")
def main():#Обьявляем новую общую функцию 
    rezyltat = two_func()#Создаем обьект
    rezyltat.first_func()#Обращаемся к первому атрибуту  обьекта
    rezyltat.second_func()##Обращаемся ко второму  атрибуту  обьекта
if __name__ == "__main__":
    main()