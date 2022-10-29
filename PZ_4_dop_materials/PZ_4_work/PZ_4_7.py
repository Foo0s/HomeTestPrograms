try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    if number_1 < number_2:
        number_3 = 0
        while number_1 <= number_2:
            number_3 += 1
            print(number_2)
            number_2 -= 1
        print('Количество чисел: ', number_3)
    else:
        print('Error')

except Exception:
    print('Error')