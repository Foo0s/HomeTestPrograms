number = int(input('Введите цифру чтобы узнать среднее арифмитическое от 1 до вашего числа: '))
list_1 = []
number_2 = 1
while range(number_2, number+1):
    try:
        list_1.append(number_2)
        number_2 += 1
        continue
    except Exception:
        print('Ошибка')
        continue
print("Среднее арифмитическое ваших чисел: ", round(sum(list_1) // len(list_1), 4))


