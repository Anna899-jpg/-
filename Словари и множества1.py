my_dict = {'Anna': 2000, 'Max': 1999}
print(my_dict)
print(my_dict.get('Alex'))
print(my_dict['Anna'])
my_dict['Denis'] = 1989
print(my_dict)
my_dict.update({'Anton': 1956,
                'Sasha': 1945})
print(my_dict)
my_dict.pop('Anton')
print(my_dict)
print(my_dict.items())

my_set = {1, 2, 2, 5, 'cat', 'dog', 'dog'}
print(my_set)
print(my_set.add(8), my_set.add(9))
print(my_set)
print(my_set.remove(1))
print(my_set)