import re

"""

验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：
用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
QQ号是5~12的数字且首位不能为0

"""
def auth_username_qq():

    username = input('请输入用户名：')
    qq = input('请输入QQ号：')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)

    if not m1:
        print('请输入有效的用户名。')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号')
    if m1 and m2:
        print('你输入的信息是有效的！')

""" 
找出一段文字中的所有手机号
"""
def getmobileforText(text):
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    
    mylist = re.findall(pattern, text)

    print(mylist)

    print('--------华丽的分割线--------')
    for temp in pattern.finditer(text):
        print(temp.group())
    print('--------华丽的分割线--------')

    m = pattern.search(text)

    while m:
        print(m.group())
        m = pattern.search(text, m.end)


def divier_word():
    poem = '床前明月光，疑似地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

def replace_text():
    sentence = '你丫的是傻逼么！我操你大爷的.Fuck you！'
    purified = re.sub('[操肏艹草曹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)

def main():
    # auth_username_qq()
    text = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    replace_text()

if __name__ == "__main__":
    main()