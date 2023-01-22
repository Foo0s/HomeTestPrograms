import string

#Задание второе.
string_from_work = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."
list_digit_from_string = [i for i in string_from_work if i in string.digits]
print(list_digit_from_string)
