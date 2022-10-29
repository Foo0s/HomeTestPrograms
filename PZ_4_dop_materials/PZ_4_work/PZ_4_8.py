try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    if number_1 < number_2:
        number_3 = 0
        while number_1 <= number_2:
            number_3 += number_1
            number_1 += 1
        print('Сумма всех чисел: ', number_3)
    else:
        print('Error')

except Exception:
    print('Error')