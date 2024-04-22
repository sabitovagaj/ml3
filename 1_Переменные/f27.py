def get_pps():    
    name = "Асанов Асан Асанович"
    age = 55
    Semya = True
    doljnost = "Профессор"
    kafedra = "Информатики и ТО"
    return name, age, Semya,doljnost,kafedra
 
 
PPS = get_pps()
print("ФИО",PPS[0])              
print("Возраст",PPS[1])             
print("Семейный ",PPS[2]) 
print("Должность",PPS[3])
print("Кафедра",PPS[4])             