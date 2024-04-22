countries = (
    ("Бишкек", 80.2, (("Ленинский",3.326), ("Октябрский", 1.718), ("Свердловский", 1.718),("Первомайский",3.326))),
    ("Ош", 56.8,(("Алайский",3.326),("Узгенский", 1.718),("Ноокатский", 1.718), ("Кара-кулжинский", 1.718),("Сузакский",3.326))),
    ("Иссык-кульский ", 102, (("Иссык-Кульский", 2.2),("Джетиогузский", 2.2),("Ак суйский", 2.2),("Тонский", 1.6),("Тюпский", 1.6)))
)
 
for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))