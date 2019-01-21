from time import sleep, time
from threading import Thread, Lock
from random import randint
from multiprocessing import Process, Queue

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_banlance = self._balance + money
            sleep(0.01)
            self._balance = new_banlance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def test_thread():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('账户余额为：¥%d元' % account.balance)


def sum():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()

    for number in number_list:
        total += number

    print(total)
    end = time()

    print('Excution time: %.3f' % (end - start))

def thread_sum():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    resut_queue = Queue()
    index = 0

    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index: index + 12500000], resut_queue))
    index += 12500000
    processes.append(p)
    p.start()

    start = time()

    for p in processes:
        p.join()

    total = 0

    while not resut_queue.empty():
        total += resut_queue.get()
    print(total)
    end = time()
    print('Excution time:' % (end - start), 's', spe='')



def task_handler(cur_list, result_queue):
    total = 0
    for number in cur_list:
        total += number
    result_queue.put(total)


def main():
    thread_sum()

if __name__ == "__main__":
    main()