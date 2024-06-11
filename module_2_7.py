values_list = [78, 'new_default', [13, 14]]
values_dict = {'a':3, 'b':6, 'c':15}
values_list_2 = ['internet', True]

def print_params(a = 4, b = 'stroka_texta', c = False):
    print (a, b)
    print (b, c)
    print (a, b, c)
    print()


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
