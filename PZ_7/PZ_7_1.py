try:
    number = int(input('Введите число: '))
    list_1 = list(str(number))
    print("Изначальное число: ", number)
    print("Символы изображающие эти цифры: ", *list_1[::-1], sep='')
except ValueError:
    print('Ошибка')
