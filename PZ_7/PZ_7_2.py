user = input('Введите строку: ')

'''Первое решение.'''
# user_string = '.'.join(user.split())
# print(user_string)

'''Второе решение.'''
string_2 = user.split()
string = ''
for i in string_2:
    if i == string_2[-1]:
        string += i
    else:
        string += i+' '
print(string.replace(' ', '.'))
