# import Function
from Function import make_pizza as mp

mp("hhff")

requested_toppings = ['mushrooms', 'onllins', 'pineapple']

# 使用 in 判断元素是否在列表中
# 使用 not in 判断元素是否不再列表中
if 'mushrooms' not in requested_toppings:
    print('mushrooms 在 requested_toppings 中')
else:
    print('mushrooms 不在 requested_toppings 中')
