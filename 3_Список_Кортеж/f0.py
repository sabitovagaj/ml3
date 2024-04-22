fakultets = (
    ("ИНИТ", 80, (("КАФ_1",23), ("КАФ_2", 12),("КАФ_3", 9))),
    ("Химфак", 66, (("Общая химия", 22),("Биохимии", 16),("Биофизика", 17)))
)
 
for fakultet in fakultets:
    fakultetName, fakultetPopulation = fakultet
    print("\nfakultet: {} Название фак: {} Количество ППС: {} ".format(fakultetName, fakultetPopulation))
    for kafedra in fak:
        kafedraName, kafedraPopulation = kafedra
        print("Kafedra: {}  Количество ППС: {} ".format(kafedraName))