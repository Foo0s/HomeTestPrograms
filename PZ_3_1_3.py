while True:
    try:
        a = int(input('Введите двухзначное число: '))
        if 10 <= a <= 99:
            b = a // 10
            c = a % 10
            v = b + c
            if v % 2 == 0:
                print(v + 2)
                break
            else:
                print(v - 2)
            break
        else:
            print('Error')
            continue
    except Exception:
        print('Error')
        continue