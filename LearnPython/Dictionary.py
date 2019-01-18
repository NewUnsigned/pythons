d = {'color': 'green', 'points': '5', 'f': 'green'}
print(d['color'])

d['level'] = 0
print(d)

del d['level']
print(d)
print('The color of word is ' +
      d['color'].title())

for key, value in d.items():
    print(key)
    print(value)

for key in d.keys():
    print(key)

for key in sorted(d.keys()):
    print(key)

# 获取所有值

for value in d.values():
    print(value)

# 去除所有重复的值

for value in set(d.values()):
    print(value)
