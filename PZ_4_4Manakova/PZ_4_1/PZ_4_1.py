while True:
    try:
        x = float(input('Введите вещественное число, оно должно быть меньше 1 и больше -1: '))
        n = int(input('Введите целое число, оно должно быть больше 0: '))
        if abs(x) > 1:
            print('Вы ввели число больше 1')
            continue
        if n < 0:
            print('Вы ввели число меньше 1')
            continue
        else:
            number = 1
            ln = x
            while number != n:
                number += 1
                if number % 2 == 0:
                    ln -= x**number / number
                else:
                    ln += x**number / number
            print(ln + (-1**n-1)*x**n / n)
        break
    except Exception:
        print('Ошибка')
        continue