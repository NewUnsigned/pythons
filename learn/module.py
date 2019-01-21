from datetime import datetime, timedelta, timezone
from collections import namedtuple, deque, defaultdict



def date_time_moudle():
    now = datetime.now()

    print(now)
    print(type(now))

    dt = datetime(2019, 1, 18)
    print(dt)
    dt.timestamp()
    dt1 = datetime.fromtimestamp(124324233223.0)

    dt2 = now + timedelta(hours=1)
    print(dt2)

""" 
namedtuple 是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple的个数
可以用属性而不是索引来引用tuple的某个元素
"""
def named_tuple_module():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(p.y)
    print(isinstance(p, Point))
    print(isinstance(p, tuple))

def deque_module():
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)

def defaultdict_module():
    add = defaultdict(lambda: 'N/A')
    add['key1'] = 'abl'
    print(add['key1'])
    print(add['key2'])


def main():
    defaultdict_module()

if __name__ == "__main__":
    main()



