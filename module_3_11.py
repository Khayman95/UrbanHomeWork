def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(1,2)
print_params()
print_params(b=25)
print_params(c = [1,2,3])

values_list = (15, 2.3, 'Скорость')
print_params(*values_list)
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}
print_params(**values_dict)

values_list_2 = (26, 9.5)
print_params(*values_list_2, 42)