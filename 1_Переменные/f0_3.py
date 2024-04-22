#! Программа Обменный пункт
usd = 68
euro = 79
uan=10
money = int(input("Введите сумму, которую вы хотите обменять: "))
currency = int(input("Укажите код валюты (доллары - 400, евро - 401,uan-300): "))
if currency == 400:
    cash = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 401:
    cash = round(money / euro, 2)
    print("Валюта: евро")
elif currency == 300:
    cash = round(money / uan, 2)
    print("Валюта: Юан")    
else:
    cash = 0
    print("Неизвестная валюта")
 
print("К получению:", cash) 
# Другой пример 
print("Для выхода нажмите Y")
 
while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break  # выход из цикла
    money = int(data)
    cache = round(money / 56, 2)
    print("К выдаче", cache, "долларов")
 
print("Работа обменного пункта завершена")   