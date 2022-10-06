#while True:
    #try:
        #a, b = int(input('Введите число: ')), int(input('Введите 2 число: '))
        #if a * b < 0:
            #print((a*b)*8)
        #else:
            #print((a*b)*1.5)
    #except Exception:
        #print('Ошибка')

### Второе задание
#l = int(input('Введите число (2 задание): '))
#if l % 2 == 0:
    #print(l // 4)
#else:
    #print(l * 5)

### Третье
while True:
    try:
        name = int(input('Введите двухзначное число: '))
        if 10 <= name <= 99:
            a = name % 10
            b = name // 10
            v = b + a
            if v % 2 == 0:
                print(v + 2)
            else:
                print(v - 2)
        else:
            print('Ошибка')
            continue
    except Exception:
        print('Гыыы')
        continue


