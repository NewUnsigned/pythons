class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("%s 正在玩飞行棋" % self._name)
        else:
            print('%s 正在玩斗地主' % self._name)


class Student(Person):
    """ 学生 """

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Teacher(Person):
    """ 老是 """

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s' % (self._name, self._title, course)



def main():
    person = Person('王大成', 12)
    person.play()
    person.age = 22
    person.play()

    stu = Student('王大成', 15, '初三')
    stu.study('数学')
    
    t = Teacher('哈哈', 38, '老教授')
    t.teach('Python程序设计')
    # 没有提供setter方法
    # person.name = '哈哈哈哈'


if __name__ == "__main__":
    main()
