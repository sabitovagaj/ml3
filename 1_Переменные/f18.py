x = [-3,2,3,5,9,1,0,2,3]

def my_min(sequence):
    """Выводит мин значение"""
    low = sequence[0] # необходимо для начального значения мин списка
    for i in sequence:
        if i < low:
            low = i
    return low

print("Минимальное число в списке равно",my_min(x)) 