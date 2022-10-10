while True:
    try:
        number = int(input('Введите целое число: '))
        if number > 0:
            print(number + 20)
            break
        else:
            print(number - 5)
            break
    except ValueError:
        print('Error')
        continue