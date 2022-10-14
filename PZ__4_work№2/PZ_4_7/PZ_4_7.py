active = True
while active:
    try:
        number_1, number_2 = int(input("Введите первое число: ")), int(input("Введите второе число: "))
        list_1 = []
        if number_1 >= number_2:
            print("\tОшибка!\n\tПервое число должно быть меньше второго!")
            continue
    except Exception:
        print("Error")
        continue
    while range(number_1 + 1, number_2 + 1):
        list_1.append(number_2)
        print(number_2)
        number_2 -= 1
        active = False
print(number_1)
list_1.append(number_1)
print('Количество ваших цифр: ', len(list_1))