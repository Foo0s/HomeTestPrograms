while True:
    try:
        a = int(input('Введите число: '))
        if a % 2 == 0:
            print(a // 4)
            break
        else:
            print(a*5)
            break
    except Exception:
        print('Error')
        continue