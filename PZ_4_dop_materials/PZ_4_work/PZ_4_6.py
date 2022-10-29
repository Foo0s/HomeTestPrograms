list_1 = []
while True:
    print('\Введите exit чтобы выйти и цикла/')
    number = input('Введите число: ')
    if number == '0':
        list_1.append(0)
    if number == 'exit':
        print(len(list_1))
        break