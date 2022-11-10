def quantity(number):
    string = str(number)
    print(len(string))
try:
    number = int(input('Введите число: '))
except ValueError:
    print('Ошибка')
else:
    quantity(number)