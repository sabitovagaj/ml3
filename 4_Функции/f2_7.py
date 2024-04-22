def factorial(num):
    """ Вычисляет факториал целого числа """
    if num < 0:
        raise RuntimeError("факториал отрицательного числа не считаем")
    fact = 1
    for i in range(2, num+1): # диапазон [2..num+1) полуоткрытый, то есть, [2..num]
        fact = fact * i
    return fact

try:
    print(factorial(0))
    print(factorial(5))
    print(factorial(-1))
except RuntimeError as err:
    print(err)