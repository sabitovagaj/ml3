def Student():
    a=input("Введите имя")
    name_vuz = "КНУ им.Ж.Баласагына"
    fak="ФИИТ"
    kaf="ИТиПрограммирования"  
    return a,name_vuz, kaf, fak

stud1 = Student()
print(stud1[0])              # Tom
print(stud1[1])              # 22
print(stud1[2])
print(stud1[3])              # False