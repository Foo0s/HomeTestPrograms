'''Ввод данных.'''
A = int(input("Введите первый член: "))
D = int(input("Введите знаменатель геометрической прогрессии: "))

list_2 = []
answer = A

def formyla(D, answer):
    i = 0
    while i != 10:
        list_2.append(answer)
        answer *= D**1
        i += 1
    print(list_2)

formyla(D, answer)

