try:
    number = int(input('Введите число: '))
    n = 1
    S = 0
    n_2 = 1
    while n <= number:
        n_2 *= n
        n += 1
        S += n_2
    print(S)
except Exception:
    print('Error')
