class mnogo_func:
    def __init__(self, name):# Данный конструктор обьединяет несколько функций
        self.name = name
    def func_1(self):
        print(self.name + "func_1")
        print("Здесь решается линейные алгебраические уравнения ")
    def func_2(self):        
        print(self.name + "func_2")
        print("Здесь решается  нелинейные алгебраические уравнения ")
def main():# Вот общая функция 
    func_class = mnogo_func("Из множества функций берем ")
    func_class.func_1()
    func_class.func_2()
if __name__ == "__main__":
    main()