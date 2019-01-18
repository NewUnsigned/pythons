def greet_user(username='HH'):
    print('Hello ' + username + '!')


# greet_user(username="ZP")
# greet_user('hh')

def get_formated_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


name = get_formated_name(last_name='jimi', first_name='hendrix')
# 没有默认值的实参必须同时有或者没有关键字
name1 = get_formated_name('jimi', 'hendrix', middle_name='oo')

print(name)


# 任意数量的参数
def make_pizza(*toppings):
    print('Making a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)


make_pizza('hh', 'eee', 'fff')


# 如果函数有不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
def make_pizza(size, *toppings):
    print('Make a ' + str(size) + ' pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)


make_pizza(12, 'hh', '3ee', 'rr')
make_pizza(16, 'dd', 'dd')
