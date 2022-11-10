def PS(a, b):
    Plosh = a * b
    Perim = (a + b)*2
    print(f"Результат....\n\tПлощадь: {Plosh}\n\tПериметр: {Perim}\n....................")
try:
    number = int(input('Введите первую сторону прямоугольника: '))
    number_2 = int(input('Введите вторую сторону прямоугольника: '))
except ValueError:
    print('Ошибка')
else:
    PS(number, number_2)