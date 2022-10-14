active = True
list_1 = []
while active:
    try:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))
        number_3 = int(input("Введите третье число: "))
        number_4 = int(input("Введите четвёртое число: "))
        if number_1 % 2 == 0:
            list_1.append(1)
        if number_2 % 2 == 0:
            list_1.append(1)
        if number_3 % 2 == 0:
            list_1.append(1)
        if number_4 % 2 == 0:
            list_1.append(1)
        print(len(list_1))
        active = False
    except Exception:
        print('Ошибка')
        continue