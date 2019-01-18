# 首字母大写的名称指的是类
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        print(self.name.title() + 'rolled over!')


dog = Dog("aa", 'bb')
dog.sit()
