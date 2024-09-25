def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

# 1 example

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# 2 example
values_list = (21, 'Danil', True)
values_dict = {'a': 52, 'b': 'Sasha', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3 example
values_list_2 = [21, 'Vlad']
print_params(*values_list_2, 42)