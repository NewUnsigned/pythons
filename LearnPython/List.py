
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(bicycles[0].title())
# 使用-1索引可以访问列表的最后一项
print(bicycles[-1])

bicycles[0] = 'haha'

del bicycles[1]

print(bicycles)

a = bicycles.pop()
bicycles.insert(1,'bb')
print(a)
print(bicycles)

for b in bicycles:
    print(b)
print(b)

for index in range(1,5):
    print(index)

squares = [value ** 2 for value in range(1,11)]
print(squares)
print(squares[100:-11])