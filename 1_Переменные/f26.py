departments = (
    ("Факультет ИПМ", 26, (("Кафедра ПМ",12), ("Кафедра информатики", 17))),
    ("Химии", 25, (("Химическая технология", 10),("Общая химия ", 12)))
)
 
for department in departments:
    departmentName, departmentPopulation, kafedry = department
    print("\nФакультет: {}  Количество сотрудников и ППС: {}".format(departmentName, departmentPopulation))
    for kafedra in kafedry:
        kafedraName, kafedraPopulation = kafedra
        print("Кафедра: {}  Количество ППС: {}".format(kafedraName, kafedraPopulation))

