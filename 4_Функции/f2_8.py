def get_user():
    name = "Асанов Асан "
    age = 64
    rabotaet="Кафедра прикладной информатики "
    is_married = True
    return name, age, rabotaet,is_married
 
 
user = get_user()
print(user[0])              # Tom
print(user[1])              # 22
print(user[2])              # False 
