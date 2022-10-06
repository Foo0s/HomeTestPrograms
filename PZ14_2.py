### Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни).
### Вариант 14. ИС-23 Sklyarov

while True:                                                     # Бесконечный цикл while - значение True
    try:                                                        # Обработчик исключений - блок который выполняется T
        numbers = int(input('Введите трехзначное число: '))     # Ввод данных - тип данных с str меняется на int
        if 100 <= numbers <= 999:                               # Условие что введённое нами значение в переменной
                                                                # входит в диапазон от 100 до 999
            print(numbers // 100)                               # вывод если True условие деление нацело numbers на 100
            break                                               # остановка цикла
        else:                                                   # Условие иначе если под условие не подходит
            print('Ошибка')                                     # Вывод - Ошибки
            continue                                            # Переход на начало цикла
    except Exception:                                           # Обработчик исключений вывод  Ошибок
        print('Ошибка')
        continue                                                # Переход на начало цикла