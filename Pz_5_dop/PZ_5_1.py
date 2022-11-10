def summa(a):
    i = 0
    max = 0
    while i < a:
        i += 1
        max += i
    list_2.append(max)
    return max

try:
    list_2 = []
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    number_3 = int(input("Введите третье число: "))
except ValueError:
    print('Error')
    
else:
    summa(number_1)
    summa(number_2)
    summa(number_3)
    if max(list_2) == summa(number_1):
        print(f'Число: {number_1}')
    elif max(list_2) == summa(number_2):
        print(f"Число: {number_2}")
    else:
        print(f"Число: {number_3}")
