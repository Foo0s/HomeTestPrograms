import random

#####ПЕРВОЕ РЕШЕНИЕ#####
    # from functools import reduce
    #
    # list_number_one = set([random.randint(-40, 50) for _ in range(random.randint(5, 13))])
    # list_number_two = set([random.randint(-20, 30) for _ in range(random.randint(6, 12))])
    # print(list_number_two)
    # print(list_number_one)
    #
    # #Первый вариант.
    # a = list(map(lambda x,y: f"{x, y}" if x != y else None, list_number_one, list_number_two))
    # print(a)
    # list_2 = [int(k) for i in a for k in i if k.isdigit() and k != None]
    # print(list_2)
    # print(sum(list_2) / len(list_2))

#####ВТОРОЕ РЕШЕНИЕ#####
list_number_one = set([random.randint(-10, 20) for _ in range(random.randint(5, 13))])
list_number_two = set([random.randint(-10, 20) for _ in range(random.randint(6, 12))])
list_test = list_number_one - list_number_two
print(list_number_one)
print(list_number_two)
print(list_test)
# Ответ
print(f"Среднее арифмитическое: {sum(list_test) // len(list_test)}")