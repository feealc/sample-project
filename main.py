import re
from test_git_submodule1.my_functions import calcular_area


if __name__ == '__main__':
    print('main')
    print('vou calcular a area')
    ret = calcular_area(10, 15)
    print(f'Area = [{ret}]')
