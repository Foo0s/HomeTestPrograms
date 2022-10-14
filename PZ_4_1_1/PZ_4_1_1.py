number_3 = 2
active = True
while active:
    try:
        number = float(input("Введите вещественное число (P.S оно должно быть меньше 1.): "))
        number_2 = int(input("Введите целое число: "))
        if number > 1:
            break
    except Exception:
        print('Опа ошибочка!')
        continue
    while number_3 <= number_2:
        a = number - (number**number_3)/number_3
        number_3 += 1
        a = number - (number**number_3)/number_3 + (number**number_3)/number_3 + (-1)**number_2-1 * number**number_2 // number_2
        active = False
print(a)
