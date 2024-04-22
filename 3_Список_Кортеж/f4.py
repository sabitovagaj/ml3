fakultets = (
    ("ФИИТ", 80, (("ИТП",23), ("КАФ", 12),("ПИ", 9))),
    ("Химфак", 66, (("Общая химия", 2.2),("Биохимии", 1.6)))
)
 
for fakultet in fakultets:
    fakultetName, fakultetPopulation, fak = fakultet
    print("\nfakultet: {}  Количество ППС: {}".format(fakultetName, fakultetPopulation))
    for kafedra in fak:
        kafedraName, kafedraPopulation = kafedra
        print("Kafedra: {}  Количество ППС: {}".format(kafedraName, kafedraPopulation))
        # for pr in prep:
        #   prepName, prepPopulation=pr
        #   print("prep: {}  ФИО ППС: {}".format(prepName, prepPopulation))