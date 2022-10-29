list_1 = []
while True:
    print('\Введите 000 чтобы выйти и цикла/')
    try:
        number = int(input('Введите число: '))
        list_1.append(number)
        if number == 000:
            list_1.pop(-1)
            print(len(list_1))
            print(sum(list_1) / len(list_1))
            break
    except Exception:
        print('Error')
