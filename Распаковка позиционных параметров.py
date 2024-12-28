def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()

print_params(False, 10, 'None')
print_params('txt', 8)
print_params("coconut")
print_params()

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [False, 101.1, 'Human']
values_dict = {'a': 13, 'b': 'apple', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Str', 7]
print_params(*values_list_2, 42)

def append_to_list(item, values_list=None):
    if values_list is None:
        values_list = []
        values_list.append(item)
    print(values_list)
