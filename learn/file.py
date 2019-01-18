
from math import sqrt

def read_file_one():
    f = None
    try:
        f = open('file.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('文件不存在')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()

# 使用with关键字指定文件的上下文环境，在离开上下文环境时，自动释放文件资源
def read_file_two():
    try:
        with open('file.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('文件不存在')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')

def read_file_three():
    with open('file.txt', mode='r') as f:
        for line in f:
            print(line, end='')

    print()

    with open('file.txt') as f:
        lines = f.readlines()
    print(lines)


def is_prime(n):
    """ 判断是否是素数 """
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def write_prime_to_file():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写入文件时发生错误')
    finally:
        for fs in fs_list:
            fs.close()

    print('操作完成')

import json

def save_jsondata():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)

    print('操作完成')


def main():
    save_jsondata()

if __name__ == "__main__":
    main()