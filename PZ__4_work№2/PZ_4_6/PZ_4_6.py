list_1 = []
while True:
    try:
        print("Введите 9999 чтобы окончить цикл.")
        number_1 = int(input('Введите целое число: '))
        if number_1 == 9999:
            print('Количество введённых 0: ', len(list_1))
            break
        if number_1 == 0:
            list_1.append(number_1)
    except Exception:
        print("Ошибка")
        continue
