active = True
spisok = []
spisok_2 = []
while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        d = int(input("Введите четвёртое число: "))
        if a < 0:
            spisok_2.append(a)
        if b < 0:
            spisok_2.append(b)
        if c < 0:
            spisok_2.append(c)
        if d < 0:
            spisok_2.append(d)
        spisok.append(a)
        spisok.append(b)
        spisok.append(c)
        spisok.append(d)
        print('Сумма чисел: ', sum(spisok))
        print(f"Количество отрицательных чисел: ", len(spisok_2))
        break
    except Exception:
        print('Ошибка!')
        continue