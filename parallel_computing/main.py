from threading import Thread
import asyncio
from multiprocessing import Process, Queue
from time import sleep


def square_num():
    lst = []
    for num in range(1, 11):
        lst.append(num ** 2)
    print(lst)

async def async_square_num():
    lst = []
    for num in range(1, 11):
        lst.append(num ** 2)
        await asyncio.sleep(.1)
    print(lst)

def cube_num():
    lst = []
    for num in range(1, 11):
        lst.append(num ** 3)
    print(lst)

def timer():
    for i in range(10):
        print(i)
        sleep(1)

def run(func_name):
    if func_name == 'count':
        thread_1 = Thread(target=square_num)
        thread_2 = Thread(target=cube_num)
    elif func_name == 'timer':
        thread_1 = Thread(target=timer)
        thread_2 = Thread(target=timer)

    thread_1.start()
    thread_2.start()

# def fact(num: int, res) -> int:
#     if num == 1:
#         res.put(1)
#         return 1
#     result = fact(num - 1, res) * num
#
#     res.put(result)
#     return result

def fact(num: int, res):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        if i == num:
            res.put(fact)

def main():
    run('count')
    run('timer')
    asyncio.run(async_square_num())
    for i in range(1, 11):
        res = Queue()
        process = Process(target=fact, args=(i, res))
        process.start()
        print(f'Факториал числа {i} = {res.get()}')


if __name__ == '__main__':
    main()