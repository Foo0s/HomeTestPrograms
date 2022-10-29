try:
    number_1 = int(input('Введите целое число: '))
    number_2 = int(input('Введите второе целое число: '))
    number_3 = int(input('Введите третье целое число: '))
    answer = number_1 + number_2*(number_3 - 1)
    if 10 < answer < 30:
        summ_number = 0
        while answer < 30:
            summ_number += 1
            answer += 1
        print('Количество значений удовлетворяющих условию:', summ_number)
    else:
        print('Error')
except Exception:
    print('Error')