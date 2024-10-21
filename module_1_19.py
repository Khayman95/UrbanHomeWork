my_dict = {'Alex' : 1995, 'Diana' : 1996, 'Alica' : 2023}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Tatyana','Нет значения'))
my_dict.update({'Tatyana' : 1963,
                'Alexandr' : 1968})
print(my_dict)
a=my_dict.pop('Alexandr')
print(my_dict)
print(a)

my_set = {12,35,12,'school',35,'appel','school'}
print(my_set)
print(my_set.add(10))
print(my_set.add(25))
print(my_set)
print(my_set.discard(12))
print(my_set)
