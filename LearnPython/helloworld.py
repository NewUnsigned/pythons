
import this

if False:
    print('hello, world')
else:
    print('hello')
    print(r"this is a line with \n")

counter = 2 ** 5
print(counter)

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
print(type(counter))
print(isinstance(counter, int))

str = 'abcdefg'
'''

'''
# 取字符串会越界
print(str[1])
# [0:8]这种方式取字符串不会越界
print(str[0:8])
print(str[0:-1])