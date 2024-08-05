def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

list = [2, "hi", True]
# 2
values_list = (5, 'cat', True)
print(values_list)

values_dict = {'a': 5, 'b': 'cat', 'c': True}
print_params(*values_list)
print_params(**values_dict)
#3
values_list_2 = (3, 'cat')
print_params(*values_list_2, 42)
print_params(b = 25)
print_params(c = [1,2,3])