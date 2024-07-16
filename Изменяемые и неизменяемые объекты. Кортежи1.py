immutable_var = 1, 'black', True
print(immutable_var)
# кортежи нельзя изменить, но они могут содержать изменяемые объекты
immutable_var = [1, 'black'], True
print(immutable_var)
immutable_var[0][0] = 5
print(immutable_var)
mutable_list = [1, 2, 3]
print(mutable_list)
mutable_list[1] = 5
print(mutable_list)