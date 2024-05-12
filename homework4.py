immutable_var = (1, 2, "War", True, [10, 19])
mutable_list = [1,2, 'War', True, [10, 10]]

print ('Неизменяймый список: ', immutable_var)

#immutable_var[2] = immutable_var[2] + 12)
#Изменять переменные в круглых скобках (Кортежи) нельзя, они постоянны,
#исключением являются переменные типа "list". Их в кортежах изменять можно

immutable_var[4][0] = immutable_var[4][0] + 3
immutable_var[4][1] = immutable_var[4][1] + 5

print ('Неизменяймый список: ', immutable_var)

print ('Изменяемый список: ', mutable_list)

mutable_list [0] = mutable_list [0] + 88
mutable_list [1] = mutable_list [1] * 12
mutable_list [2] = (mutable_list [2] + 'tunder') * 2
mutable_list.remove(True)
print ('Изменяймый список: ', mutable_list)
