def sum(*params):
    result = 0
    for n in params:
        result += n
    return result
 
 
sumOfNumbers1 = sum(1, 2, 3, 4, 5,-4,-68,798,999,-445,876)      # 15
sumOfNumbers2 = sum(3, 4, 5, 6,8,4568,876)         # 18
print("Сумма чисел sumOfNumbers1 равно=",sumOfNumbers1)
print("Сумма чисел sumOfNumbers1 равноsumOfNumbers2=",sumOfNumbers2)
print("Средне арифметическое чисел  sumOfNumbers1 равноsumOfNumbers2 равно=",(sumOfNumbers2+sumOfNumbers1)/2)