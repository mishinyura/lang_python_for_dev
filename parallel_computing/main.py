from threading import Thread
import asyncio
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


def main():
    run('count')
    run('timer')
    asyncio.run(async_square_num())

if __name__ == '__main__':
    main()