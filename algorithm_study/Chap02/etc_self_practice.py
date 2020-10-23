import copy

x = [[1,2,3],[4,5,6]]
x_copy = x.copy()
x_deepcopy = copy.deepcopy(x)
x_equal = x
x[0][1] = 0
print(f'x_copy = {x_copy}')
print(f'x_deepcopy = {x_deepcopy}')
print(f'x_equal = {x_equal}')